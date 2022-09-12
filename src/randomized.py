import pandas as pd
import enchant
import secrets # cryptographic-level randomness
import time
import plotly.graph_objects as go

d = open("/usr/share/dict/words", "r").read().splitlines()
d_verify = enchant.Dict("en_US")

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def random_letter_draw():
    letters = [secrets.choice(alphabet) for _, val in enumerate(range(1, 8))]
    center_letter = secrets.choice(letters)

    matches = list()

    start = time.time()
    for word in d:
        if len(list(word)) >= 4 and center_letter in list(word):
            l_sum = 0
            for l in list(word):
                if l in letters:
                    l_sum += 1
            if l_sum == len(word):
                matches.append(word)

    stop = time.time()

    for word in matches:
        if not d_verify.check(word):
            matches.remove(word)

    return ''.join(letters), len(matches), (stop-start)

l, m, t = random_letter_draw()

def multiple_draws(n=5):
    data_outline = {
        "draw_number": [],
        "letters": [],
        "matches": [],
        "time": []
    }
    df = pd.DataFrame(data_outline)

    for idx, val in enumerate(range(1, n+1)):
        l, m, t = random_letter_draw()
        df.loc[idx, "draw_number"] = val
        df.loc[idx, "letters"] = l
        df.loc[idx, "matches"] = m
        df.loc[idx, "time"] = t

    return df

bulk_draws = [multiple_draws(n=100) for _, val in enumerate(range(1, 6))]

for idx, draw in enumerate(bulk_draws):
    draw['set_number'] = f"Set {idx+1}"

layout = go.Layout(
    paper_bgcolor='rgba(255,255,255,100)',
    plot_bgcolor='rgba(255,255,255,100)'
)
fig = go.Figure(layout=layout)

colors = [
    "#C0DFA1",
    "#9FC490",
    "#82A3A1",
    "#465362",
    "#011936"
]

for idx, draw_set in enumerate(bulk_draws):
    fig.add_trace(go.Violin(
        x=draw_set.set_number,
        y=draw_set.matches,
        line_color=colors[idx],
        box_visible=True,
        meanline_visible=True,
        showlegend=False,
        x0='Real Words from Randomly Generated 7-letter set'
    ))

fig.update_layout(title_text="Distribution of Real Word Matches from Randomly Generated 7-Letter Set")
fig.update_yaxes(title_text="# Real Words Found")
fig.show()

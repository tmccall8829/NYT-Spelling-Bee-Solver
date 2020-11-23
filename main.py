from itertools import product
import enchant

# define our spell-checking dictionary
d = enchant.Dict("en_US")

# letters from the game
#letters = list("aoputcn")
letters = list("cpanyoh")
# necessary letter all words must contain
#center_letter = "n"
center_letter = "y"
all_words = []

print("Analyzing generated pseudo-words...")
for i in range(4, 8):
    print("---> Target: {}-letter words".format(i))
    for c in product(letters, repeat = i):
        word = ''.join(c)
        # print(word)
        if center_letter in word and d.check(word):
            all_words.append(word)

print("Found {} words: {}".format(len(all_words), all_words))

# Now let's check to see if we got the pandrome in our all_words list!
pandromes = list()
for w in all_words:
    if all(c in w for c in letters):
        print("Found pandrome: {}".format(w))
        pandromes.append(w)

# If we didn't find a pandrome, try a longer combination. After 7 letters, the
# time it takes to generate the certesian product increases substantially
if len(pandromes) == 0:
    print("Pandrome is longer than 7 letters. Generating 8-letter words...")
    print("This will take some time.")

c_8 = product(letters, repeat = 8)
for c in c_8:
    word = ''.join(c)
    # print(word)
    if center_letter in word and d.check(word):
        print("Found an 8-letter word: {}".format(word))
        all_words.append(word)

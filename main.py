from itertools import product
import enchant
import time

# define our spell-checking dictionary
d = enchant.Dict("en_US")

# letters from the game
letters = list("aoputcn")

# necessary letter all words must contain
center_letter = "n"

all_words = []

print("Analyzing generated pseudo-words...")
for i in range(4, 10):
    print("---> Target: {}-letter words".format(i))
    start = time.time()
    for c in product(letters, repeat = i):
        word = ''.join(c)
        if center_letter in word and d.check(word):
            all_words.append(word)
    stop = time.time()
    print("Analysis time: {}".format(stop - start))

print("Found {} words: {}".format(len(all_words), all_words))

# Now let's check to see if we got the pandrome in our all_words list!
pandromes = list()
for w in all_words:
    if all(c in w for c in letters):
        print("Found pandrome: {}".format(w))
        pandromes.append(w)

# If we didn't find a pandrome, we could try a longer combination.
# After 7 letters, though, the time it takes to check all of the certesian
# products increases substantially, so I just stop here.
if len(pandromes) == 0:
    print("Pandrome is longer than 9 letters. I don't check that many. Sorry :(")

from itertools import product
import enchant
import time

# define our spell-checking dictionary
d = enchant.Dict("en_US")

# letters from the game
letters = list("tliudeg")

# necessary letter all words must contain
center_letter = "g"

all_words = []

print("Analyzing generated pseudo-words...")
i = 4
while i <= 9:
    print("---> Target: {}-letter words".format(i))
    start = time.time()
    for c in product(letters, repeat = i):
        word = ''.join(c)
        if center_letter in word and d.check(word): # d.check() adds a ton of computation time!
            all_words.append(word)
    stop = time.time()
    print("Analysis time: {}".format(stop - start))
    i += 1

print("Found {} words: {}".format(len(all_words), all_words))

# Print some data about word lengths
sum_4 = 0
sum_5 = 0
sum_6 = 0
sum_7 = 0
sum_8 = 0
sum_9 = 0
for w in all_words:
    if len(w) == 4:
        sum_4 += 1
    elif len(w) == 5:
        sum_5 += 1
    elif len(w) == 6:
        sum_6 += 1
    elif len(w) == 7:
        sum_7 += 1
    elif len(w) == 8:
        sum_8 += 1
    else:
        sum_9 += 1

print("There are {} 4-letter words.".format(sum_4))
print("There are {} 5-letter words.".format(sum_5))
print("There are {} 6-letter words.".format(sum_6))
print("There are {} 7-letter words.".format(sum_7))
print("There are {} 8-letter words.".format(sum_8))
print("There are {} 9-letter words.".format(sum_9))

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

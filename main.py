from itertools import combinations_with_replacement
import enchant

# define our spell-checking dictionary
d = enchant.Dict("en_US")

# letters from the game
letters = list("aoputcn")

# necessary letter all words must contain
center_letter = "n"

# programmatically grab the vowels from the letter list
possible_vowels = list("aeiouy")
vowels = list()
for v in possible_vowels:
    if v in letters:
        vowels.append(v)

print("Found vowels: {}".format(vowels))

print("Generating combinations...")
c_4 = combinations_with_replacement(letters, 4)
c_5 = combinations_with_replacement(letters, 5)
c_6 = combinations_with_replacement(letters, 6)
c_7 = combinations_with_replacement(letters, 7)

all_words = []

print("Analyzing generated pseudo-words...")
# there are two conditions we know for sure:
# 1. each word must contain the center letter
# AND
# 2. each word must contain at least one vowel. duh!
# also note that words must be at least 4 letters long
for c in c_4:
    if center_letter in c and any(l in c for l in vowels):
        all_words.append(c)

for c in c_5:
    if center_letter in c and any(l in c for l in vowels):
        all_words.append(c)

for c in c_6:
    if center_letter in c and any(l in c for l in vowels):
        all_words.append(c)

for c in c_7:
    if center_letter in c and any(l in c for l in vowels):
        all_words.append(c)

print(all_words)

real_words = list()
for word in all_words:
    if d.check(word):
        real_words.append(word)

print(real_words)

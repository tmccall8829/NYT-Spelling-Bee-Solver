import time
import enchant

d = open("/usr/share/dict/words", "r").read().splitlines()
d_verify = enchant.Dict("en_US")

print("Enter all of the prompts using lowercase letters.")
print("Make sure to enter today's letters as a single string.")

letters = input("What are today's letters? ")
center_letter = input("What is the center letter? ")

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

print(matches)
print("Time: {}".format(stop - start))

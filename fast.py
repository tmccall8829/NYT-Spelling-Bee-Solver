import time


def process_matches(letters, center_letter, verify_matches: bool = False) -> list[str]:
    # use the built-in system dictionary on unix systems
    # to simplify things, this has been saved in the root dir
    d = open("words", "r").read().splitlines()

    matches = []
    for word in d:
        if len(list(word)) >= 4 and center_letter in list(word):
            l_sum = 0
            for l in list(word):
                if l in letters:
                    l_sum += 1
            if l_sum == len(word):
                matches.append(word)

    if verify_matches:
        import enchant

        d_verify = enchant.Dict("en_US")
        for word in matches:
            if not d_verify.check(word):
                matches.remove(word)

    return matches


if __name__ == "__main__":
    import time  # we don't care about timing unless we're calling directly

    print("Enter all of the prompts using lowercase letters.")
    print("Make sure to enter today's letters as a single string.")

    # type checking is for nerds
    letters = ""
    while len(letters) != 7:
        letters = input("What are today's letters? ")

    center_letter = ""
    while len(center_letter) != 1:
        center_letter = input("What is the center letter? ")

    # start timing after we get user input
    start = time.time()

    matches = process_matches(letters=letters, center_letter=center_letter)

    print(matches)
    print(f"{len(matches)} matches in {time.time() - start}")

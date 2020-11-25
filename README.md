# NYT-Spelling-Bee-Solver
A short program that finds every possible solution to the daily NYT Spelling Bee puzzle.

There are two methods included:
### 1. Fast
The fast method uses the native text-based dictionary present on all Unix systems. The algorithm
sifts through all of the words, filtering out words that don't:
- contain the center letter
- have four or more letters
To double-check, the algorithm then verifies the solutions using `pyenchant`.

### 2. Slow
The slow algorithm uses two python libraries: `itertools` and `pyenchant`, and it's simple:
- Input a list of letters, specifying which letter is in the center (i.e., which letter must be in every word)
- Generate all possible combinations of the given letters, from lengths 4 to 9
- Filter all of the generated words using pyenchant

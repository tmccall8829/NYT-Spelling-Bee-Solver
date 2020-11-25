# NYT-Spelling-Bee-Solver
A short program that finds (almost) every possible solution to the daily NYT Spelling Bee puzzle.

Note that neither method is guaranteed to find all possible solutions, due to
the inconsistency of the various dictionaries available. The fast method often
includes a lot of words that won't be accepted by NYT. The slow method doesn't
include as many false positives, but it also isn't guaranteed to find every word (dictionaries are surprisingly inconsistent!).

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

# NYT-Spelling-Bee-Solver
A short program that finds every possible solution to the daily NYT Spelling Bee puzzle.

The algorithm uses two python libraries: `itertools` and `pyenchant`, and it's simple:
1. Input a list of letters, specifying which letter is in the center (i.e., which letter must be in every word)
2. Generate all possible combinations of the given letters, from lengths 4 to 7
3. Filter all of the generated words using pyenchant
  

# cipher-challenge-2024
### General plan:
- prepare for the cipher challenge of 2024
- write preliminary code in python (for now)
- convert code to C++ (once I learn it)
### Linguistic data
#### English Data (open to be forked)
* English corpus (brown corpus with only characters)
* English character frequencies (EnglishMonograms.json)
* English Quadgrams
* List of words
  - ordered alphabetically (wordsAlpha.json)
  - ordered by frequency (wordsFreq.json)
#### Text Evaluation (rather not be forked until 2025)
- process text (process(text))
- calculate possible ngrams (possibleNgrams(size of n))
- find all ngrams in a text (ngrams(text, size of n))
- sort a dictionary by frequency (sortDictFreq(dictionary))
- calculate the dot product of two dictionary's frequencies (dotProduct(vector1,vector2))
- calculate the X statistic (Xstat(text, monogram frequency of English))
- calculate the angle fitness (angleFitness(text, monogram frequency of English))
- calculate the tetragram fitness (tetragramFitness(text, ngram frequency of English, size of n))
- calculate index of coincidence (IoC(text, size of n))
- calculate the entropy (entropy(text, monogram frequency of English))

# cipher-challenge-2024
## Current Workings
### monoalphabetic substitution ciphers
- write a script to go through monoalphabetic substitution cipher by hand
- write a script to draw a bar chart of English frequencies vs ciphertext frequencies

## Already done
### linguistic data
#### files
* English corpus (Brown corpus)
* English monograms 
* English quadgrams
* English words:
    - sorted alphabetically
    - sorted by frequency

#### functions
##### assorted functions
- sortDictFreq(dictionary) takes a dictionary with frequency as its value and sorts it by highest to lowest value 
- dotProduct(vector1,vector2) takes 2 dictionaries and calculates the dot product of them, required for angleFitness, returns float
##### both opening functions do not requre a file type suffix (will allow for both to assume file directories with no input later)
- process(file) takes a file name (assumes it's in the main file directory) and processes it ready for interpretation
- openDict(file,area) takes a file name (must be json) and where it is located and turns it into a dictionary
##### n grams
- possibleNgrams(size) takes size of ngram and generates all possible ngrams of that size, returns list
- ngrams(text,size) takes text and the size of ngrams and generates all ngrams along with their frequency, returns dictionary
##### fitness
- Xstat(text,fitness) takes text and English monogram frequency, returns float (closer to 0, closer to English)
- angleFitness(text,frequency) takes text and English monogram frequency, returns float between 0 and 1 (closer to 0, closer to English)
- ngramFitness(text,frequency,size) takes text and English ngram frequency (4 with English quadgrams) as well as size of ngrams (4), returns float (closer to 0, closer to English)
##### other analytics
- IoC(text,size) find the index of coincidence of a given text (English IoC is around 1.75, for IoC1)
- entropy(text) find the entropy (randomness) of a text (English entropy around 0.88 to 0.90)

### monoalphabetic substitution ciphers
#### functions
##### assorted functions
- test4MonoAlpha(text,frequency) takes text and English monogram frequency and returns boolean as to whether a ciphertext has been enciphered using a monoalphabetic substitution cipher
- invertKey(key) takes a key and inverts it so it can be used for decryption
- encipherMonoAlpha(text,key) takes plaintext and a key and returns ciphertext
- decipherMonoAlpha(text,key) takes ciphertext and a key (not inverted) and returns a plaintext 


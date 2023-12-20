'''library imports'''
import math
import json

'''functions'''
# process the text to be analysed and messed with
def process(text):
    newText = ""
    for each in text:
        if each.isalpha():
            newText += each.upper()
    return newText

# generates ngrams from given text and specified length
def ngrams(text,size):
    ngramFreq = {}
    count = 0
    for i in range(len(text)-size):
        ngram = text[i:i+size]
        if ngram not in ngramFreq:
            ngramFreq[ngram] = 1
        else:
            ngramFreq[ngram] += 1
        count += 1
    for each in ngramFreq:
        ngramFreq[each] /= count
    return ngramFreq

# sorts a given dictionary based on value (from highest to lowest)
def sortDictFreq(dictionary):
    newDictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return newDictionary

# calculcates the dot product of two dictionaries
def dotProduct(vector1,vector2):
    product = 0
    for each in vector1:
        product += vector1[each]*vector2[each]
    return product

# takes text and English monogram frequency, returns float (closer to 0, closer to English)
def Xstat(text,frequency):
    monograms = ngrams(text,1)
    X = 0
    for each in monograms:
        X += ((monograms[each]-frequency[each])**2)/frequency[each]
    return(X)

# takes text and English monogram frequency, returns float between 0 and 1 (closer to 0, closer to English)
def angleFitness(text,frequency):
    monograms = ngrams(text,1)
    cosTheta = dotProduct(monograms,frequency)/math.sqrt(dotProduct(monograms,monograms)*dotProduct(frequency,frequency))
    Theta = math.acos(cosTheta)
    return Theta

# takes text and English ngram frequency (likely 4), returns float (closer to 0, closer to English)
def tetragramFitness(text,frequency,size):
    tetragrams = ngrams(text,size)
    fitness = 0
    for each in tetragrams:
        if each in frequency:
            fitness += math.log10(frequency[each])
    fitness /= len(tetragrams)
    fitness = 10**fitness
    return fitness


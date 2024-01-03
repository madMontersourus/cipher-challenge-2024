'''library imports'''
import math
import json
from itertools import product

'''functions'''
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

# process the text to be analysed and messed with
def process(file, area=None):
    if area == None:
        text = open(file+".txt","r").read()
    else:
        text = open(area+"/"+file+".txt","r").read()
    newText = ""
    for each in text:
        if each.isalpha():
            newText += each.upper()
    return newText

# opens a dictionary 
def openDict(file,area="EnglishData"):
    if area == None:
        dictionary = dict(json.loads(open(file+".json","r").read()))
    else:
        dictionary = dict(json.loads(open(area+"/"+file+".json","r").read()))
    return dictionary

# generate a list of all possible ngrams
def possibleNgrams(size):
    ngramList = list(map("".join, product(alphabet, repeat = size)))
    return ngramList

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
def ngramFitness(text,frequency,size):
    ngram = ngrams(text,size)
    fitness = 0
    for each in ngram:
        if each in frequency:
            fitness += math.log10(frequency[each])
    fitness /= len(ngram)
    fitness = 10**fitness
    return fitness

# find the index of coincidence of a given text (English IoC is around 1.75, for IoC1)
def IoC(text,size):
    res = possibleNgrams(size)
    N = len(text)
    index = 0
    for i in res:
        index += (text.count(i)*(text.count(i)-1))/(N*(N-1))
    index *= 26**size
    return index

# find the entropy (randomness) of a text (English entropy around 0.88 to 0.90)
def entropy(text):
    monograms = ngrams(text,1)
    Sum = 0
    for each in monograms:
        Sum += monograms[each]*math.log(monograms[each],26)
    Sum *= -1
    return Sum

'''definitions'''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
monogramFrequency = openDict("EnglishMonograms")
tetragramFrequency = openDict("EnglishQuadgrams")
text = process("trialText")

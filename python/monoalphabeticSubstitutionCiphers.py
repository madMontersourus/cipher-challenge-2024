'''Criteria for a monoalphabetic substitution cipher:
- Index of coincidence is close to 1.75
- Monogram fitness is low'''

'''library imports'''
from textEvaluation import process, openDict, IoC, Xstat, alphabet

'''definitions'''
test = process("trialText")
monogramFitness = openDict("EnglishMonograms","EnglishData")

'''functions'''
# tests to see in the cipher is a monoalphabetic substitution cipher
def test4MonoAlpha(text, frequency):
    tempIoC = IoC(text, 1)
    fitness = Xstat(text, frequency)
    if tempIoC > 1.65 and tempIoC < 1.85 and fitness > 0.5:
        return True
    else:
        return False
    
# inverts the key of a monoalphabetic substitution cipher
def invertKey(key):
    correspond = {}
    newKey = ""
    for i in range (0,26):
        correspond[key[i]]=alphabet[i]
    correspond = dict(sorted(correspond.items()))
    for each in correspond:
        newKey += correspond[each]
    return newKey

# encodes a monoalphabetic substitution cipher using a key
def encipherMonoAlpha(text,key):
    ciphertext = ""
    for each in text:
        ciphertext += key[alphabet.index(each)]
    return ciphertext

# decodes a monoalphabetic substitution cipher using a key
def decipherMonoAlpha(text,key):
    plaintext = ""
    invKey = invertKey(key)
    for each in text:
        plaintext += invKey[alphabet.index(each)]
    return plaintext

def decipherMonoAlphaHand(text):
    key = alphabet.lower()
    complete = False
    print(text)
    print(key)
    while not complete:
        switch = input("Ciphertext character (capital) to plaintext character (lowercase), ie A to n written as An \n")
        index = alphabet.find(switch[1].upper())
        key = key[:index]+switch[0]+key[index+1:]
        newText = text
        for each in key:
            if each.isupper:
                new = alphabet[key.find(each)].lower()
                newText = newText.replace(f"{each}",f"{new}")
        print(newText)
        print(key)
        if key.upper() == key:
            complete = True
    return newText



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

key = "QWERTYUIOPASDFGHJKLZXCVBNM"
print(decipherMonoAlpha(test,key))

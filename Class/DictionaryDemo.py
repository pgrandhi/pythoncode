from collections import defaultdict

def letter_frequency_default(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] +=1

    return frequencies

def letter_frequency(sentence):
    frequencies={}
    for letter in sentence:
        frequencies.setdefault(letter,0)
        frequencies[letter] +=1

    return frequencies

d = letter_frequency("I love Icecream")
for letter, frequency in d.items():
    print("{} occurs {} time(s).".format(letter,frequency))

d2 = letter_frequency("I love Icecream2")
for letter, frequency in d2.items():
    print("{} occurs {} time(s).".format(letter,frequency))


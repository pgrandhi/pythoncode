def letter_frequency(sentence):
    frequencies={}
    for letter in sentence:
        frequencies.setdefault(letter,0)
        frequencies[letter] +=1

    return frequencies

d = letter_frequency("I love Icecream")
for letter, frequency in d.items():
    print("{} occurs {} time(s).".format(letter,frequency))


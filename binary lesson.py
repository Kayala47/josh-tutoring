
#Binary  Word Decoder
#01010101010 -> word
#word -> 01010101010

#primitives
#hey, this was Kevin
# hi my name is josh

letterDictionary = {
    'A': 10111110,
    'B': 10111101,
    'C': 10111100,
    'D': 10111011,
    'E': 10111010,
    'F': 10111001,
    'G': 10111000,
    'H': 10110111,
    'I': 10110110,
    'J': 10110110,
    'K': 10110100,
    'L': 10110011,
    'M': 10110010,
    'N': 10110001,
    'O': 10110000,
    'P': 10101111,
    'Q': 10101110,
    'R': 10101101,
    'S': 10101100,
    'T': 10101011,
    'U': 10101010,
    'V': 10101001,
    'W': 10101000,
    'X': 10100111,
    'Y': 10100110,
    'Z': 10100101,
    ' ': " " 
    
}

binaryDictionary = {

}

for key in letterDictionary:


    value = binaryDictionary.get(key)

    # add a key to the dictionary:
    #dictionary[key] = value
    #flip: dictionary[value] = key
    binaryDictionary[value] = key
    
    
for key in binaryDictionary:
    print("key is " + str(key))
    print("value is " + binaryDictionary.get(key))

    
#command to get a value out of a dictionary:

'''
Dictionary:

Holds two values at a time. (Key,Value)]
To get the value, use the key. dictionary.get(key) = value

000111 + 111000 = 111111
'000111' + '111000' = 000111111000

'''

# "word" = "w" + "o" + "r" + "d"

'''
def word_to_binary(word):

    capitalWord = word.upper()
    string = ""
    
    for char in capitalWord:
        print(char)
        string = string + str(letterDictionary.get(char))

    print(string)


#here is where we do the work
word = input('What do you want to turn into binary?')

word_to_binary(word)
        
'''

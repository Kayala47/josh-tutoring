
#Binary  Word Decoder
#01010101010 -> word
#word -> 01010101010

#primitives

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


    value = letterDictionary.get(key)

    # add a key to the dictionary:
    #dictionary[key] = value
    #flip: dictionary[value] = key
    binaryDictionary[value] = key
    
'''
for key in binaryDictionary:
    print("key is " + str(key))
    print("value is " + binaryDictionary.get(key))
'''
    
#command to get a value out of a dictionary:

'''
Dictionary:

Holds two values at a time. (Key,Value)]
To get the value, use the key. dictionary.get(key) = value

000111 + 111000 = 111111
'000111' + '111000' = 000111111000

'''

# "word" = "w" + "o" + "r" + "d"


def word_to_binary(word):

    #capitalizes the word so that we have standard way to access dictionary
    capitalWord = word.upper()

    #creates a string to hold our answer
    string = ""

    #loop through every character (letter) in word
    for char in capitalWord:

        #prints out the character (for testing)
        print(char)

        #adds the binary that we get from that letter to our answer
        string = string + str(letterDictionary.get(char))

    print(string)


#here is where we do the work
word = input('What do you want to turn into binary?')

word_to_binary(word)


def binary_to_word(binaryNumber):

    '''
    string = str(binaryNumber)

    for num in binaryNumber:
        string = string + str(binaryDictionary.get(num))

    print(string)
    '''

    #turn binaryNumber into a string
        #changing from one object type to another is called CASTING

    inputString = str(binaryNumber)
    
    #make another string to hold the answer
    outputString = ""

    #make a loop that goes through and touches only every 8th number
        #add to the answer string from the value we get in binaryDictionary

    # we will need a nested array
    outsideList = ()

    
    for letter in inputString:
        insideList = ()

        insideList.add(letter)

        if (insideList.size() == 8):
            #start new inside list

            outsideList.add(insideList)
            
        

        
    #print the answer out as a string

    
        #every 8 letters!
    #have to turn the number into a string first


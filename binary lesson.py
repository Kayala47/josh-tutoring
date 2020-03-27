
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

#this is flipping the letterDictionary to turn into binaryDictionary
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
    insideList = []

    for letter in inputString:
        
        insideList.append(letter)

        if (len(insideList) == 8):
            #turn back into numbers
            number = int("".join(insideList))

            #translate that section
            outputString = outputString + binaryDictionary.get(number)
            
            #erase the old list
            insideList.clear()

            
    #print the answer out as a string
    print(outputString)

    
        #every 8 letters!
    #have to turn the number into a string first

def main():

    userInput = input("What do you want to do? Binary to word (1) or word to binary (2)")

    answer = int(userInput)
    
    if answer == 1:
        #binary to word
        binaryNum = int(input("input the number here"))

        binary_to_word(binaryNum)

    elif(answer == 2):
        #word to binary
        inputWord = input("input the word here")

        word_to_binary(inputWord)
        
    else:
        #neither of those were entered
        print("Error: please choose '1' or '2'")
        main()
    

main()

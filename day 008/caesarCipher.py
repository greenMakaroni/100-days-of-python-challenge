# Day 8 final challenge
# implement caesar cipher

import re
from logo import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat = True

def caesar(text, shift, direction):
    regex = re.compile('[@_!#$% ^&*()<>?/\|}{~:]')
    password = ""
    for i in range(0, len(text)):
        letter = text[i]
        if letter.isnumeric() or regex.search(letter) != None:
            password = password + letter
        else:
            aplh_index = alphabet.index(letter)
            if direction == "encode":
                if (aplh_index + shift) > 26:
                    shifted_letter = alphabet[(aplh_index + shift) - 26]
                    password = password + shifted_letter
                else:    
                    shifted_letter = alphabet[aplh_index + shift]
                    password = password + shifted_letter
            elif direction == "decode":
                if (aplh_index - shift) < 0:
                    shifted_letter = alphabet[26 + (aplh_index - shift)]
                    password = password + shifted_letter
                else:
                    shifted_letter = alphabet[aplh_index - shift]
                    password = password + shifted_letter
            else: 
                print("Wrong input please try again")
    return password

def repeat_question():
    global repeat
    repeatOption = input("Do you want to go at it again? 'yes' / 'no': ")
    if repeatOption == "no":
        repeat = False
    elif repeatOption != "yes":
        print("Wrong input try again\n")
        repeat_question()

while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(caesar(text=text, shift=shift, direction=direction))

    repeat_question()







    #todo-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#todo-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
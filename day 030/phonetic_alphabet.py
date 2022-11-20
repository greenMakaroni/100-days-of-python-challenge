import pandas
file = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_data_frame = pandas.DataFrame(file)

nato_alphabet_dict = { row.letter : row.code for (index, row) in file.iterrows() }
print(nato_alphabet_dict)

def generatePhonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_list = [nato_alphabet_dict[f"{letter}"] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generatePhonetic()
    else:
        print(phonetic_list)

generatePhonetic()

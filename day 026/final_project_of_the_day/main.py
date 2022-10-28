

import pandas
file = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(file)


alphabet_data_frame = pandas.DataFrame(file)
#print(alphabet_data_frame)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_alphabet_dict = { row.letter : row.code for (index, row) in file.iterrows() }
print(nato_alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
phonetic_list = [nato_alphabet_dict[f"{letter.upper()}"] for letter in user_input]
print(phonetic_list)


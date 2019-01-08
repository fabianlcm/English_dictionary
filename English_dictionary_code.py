# json file reader
import json
# get_close_matches compares two arguments and returns similarities that are above the 80% mark
from difflib import get_close_matches as is_similar
# speech capabilities
from gtts import gTTS
import playsound
# operating system access
import os

# importinn json file, it can be found within this project
english_definitions = json.load(open("english_definitions.json"))

# creating tags to distinguish computer (Leo) with user (You)
leo_tag = '[Leo] '
user_tag = '[You] '

def english_dictionary(word):
    # checkng if either the upper, lower, o title form of the word is in the dictionary
    if word.lower() in english_definitions:
        return english_definitions[word]
    elif word.title() in english_definitions:
        return english_definitions[word]
    elif word.upper() in english_definitions:
        return english_definitions[word]
    
    # suggesting words based on similarity with original input
    elif len(is_similar(word, english_definitions.keys())) > 0:
        yes_no = input(leo_tag + "Did you mean '{}' instead?: ".format(is_similar(word, english_definitions.keys())[0]))
        
        # asking user to enter yes/no if word is okay or not
        if is_similar(yes_no.lower(), ['y', 'ye', 'yes', 'yeah']):
            return english_definitions[is_similar(word, english_definitions.keys())[0]]
        elif is_similar(yes_no.lower(), ['n', 'no', 'nope']):
            return leo_tag + "The word doesn't exist. Please double check it."
        
        else:
            return leo_tag + "We didn't understand your entry."

    else:
        return leo_tag + "The word doesn't exist. Please double check it."


word = input(user_tag + "Enter word: ")
output = english_dictionary(word)

# some words have more than one definition
if type(output) == list and len(output) > 1:
    counter = 1
    for element in output:
        message = "English definition # {} of '{}': ".format(counter, word) + element
        print(leo_tag + message)
        counter += 1
        
# (bug?) although some words only have one definition, they still come in list type               
elif type(output) == list and len(output) == 1:
    print(leo_tag + "English definition of '{}': ".format(word) + output[0])
    
else:
    print(leo_tag + "English definition of '{}': ".format(word) + output)

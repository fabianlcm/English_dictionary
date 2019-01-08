# json file reader
import json
# get_close_matches compares two arguments and returns similarities that are above the 80% mark
from difflib import get_close_matches as is_similar
# speech capabilities
from gtts import gTTS
import playsound
# operating system access
import os

# importing json file found in this repository
english_definitions = json.load(open("english_definitions.json"))

# creating tags to distinguish Leo with user
leo_tag = '[Leo] '
user_tag = '[You] '

def english_dictionary(word):
    if word.lower() in english_definitions:
        return english_definitions[word]
    elif word.title() in english_definitions:
        return english_definitions[word]
    elif word.upper() in english_definitions:
        return english_definitions[word]

    elif len(is_similar(word, english_definitions.keys())) > 0:
        yes_no = input(leo_tag + "Did you mean '{}' instead?: ".format(is_similar(word, english_definitions.keys())[0]))
        if is_similar(yes_no.lower(), ['y', 'yes', 'yeah']):
            return english_definitions[is_similar(word, english_definitions.keys())[0]]
        elif is_similar(yes_no, ['n', 'no', 'nope']):
            return leo_tag + "The word doesn't exist. Please double check it."
        else:
            return leo_tag + "We didn't understand your entry."

    else:
        return leo_tag + "The word doesn't exist. Please double check it."


word = input(user_tag + "Enter word: ")
output = english_dictionary(word)

if type(output) == list and len(output) > 1:
    counter = 1
    for element in output:
        message = "English definition # {} of '{}': ".format(counter, word) + element
        print(leo_tag + message)
        counter += 1
elif type(output) == list and len(output) == 1:
    print(leo_tag + "English definition of '{}': ".format(word) + output[0])
else:
    print(leo_tag + "English definition of '{}': ".format(word) + output)

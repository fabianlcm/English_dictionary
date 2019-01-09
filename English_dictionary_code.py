# json file reader
import json
# get_close_matches compares two arguments and returns similarities that are above the 80% mark
from difflib import get_close_matches as similarity_between

# importing json file, it can be found within this project
english_definitions = json.load(open("english_definitions.json"))

# creating tags to distinguish computer [Leo] with user [You]
leo_tag = '[Leo] '
user_tag = '[You] '

def english_dictionary(word):
    # checking if the lower case form of word is in the dictionary
    if word.lower() in english_definitions:
        return english_definitions[word]
    
    # checking if the title form of word is in the dictionary
    elif word.title() in english_definitions:
        return english_definitions[word]
    
    # checking if the upper case form of word is in the dictionary
    elif word.upper() in english_definitions:
        return english_definitions[word]
    
    # suggesting words when there is similarity above 0% between word and keys of the dictionary
    elif len(similarity_between(word, english_definitions.keys())) > 0:
        yes_no = input(leo_tag + "Did you mean '{}' instead?: ".format(similarity_between(word, english_definitions.keys())[0]))
        
        # asking user to enter yes if the suggested word is the expected output
        if similarity_between(yes_no.lower(), ['y', 'ye', 'yes', 'yeah']):
            return english_definitions[similarity_beween(word, english_definitions.keys())[0]]
        
        # asking user to enter yes/no if the suggested word is the expected output
        elif similarity_between(yes_no.lower(), ['n', 'no', 'nope']):
            return leo_tag + "The word doesn't exist. Please double check it."
        
        # if user input is invalid
        else:
            return leo_tag + "We didn't understand your entry."
        
    # for everything else where there is 0% similarity between word and keys of the dictionary
    else:
        return leo_tag + "The word doesn't exist. Please double check it."

    
# displaying main message to enter word
word = input(user_tag + "Enter word: ")
# creating instance
output = english_dictionary(word)

# some words have more than one definitio, therefore they come in form of a list [definition_1, definition_2, ...]
if type(output) == list and len(output) > 1:
    counter = 1
    for definition in output:
        message = "English definition # {} of '{}' is: ".format(counter, word) + definition
        print(leo_tag + message)
        counter += 1
        
# (bug?) although some words only have one definition they still come in list type              
elif type(output) == list and len(output) == 1:
    print(leo_tag + "English definition of '{}' is: ".format(word) + output[0])

# for everything else when definition does not come in list type
else:
    print(leo_tag + "English definition of '{}' is: ".format(word) + output)
    

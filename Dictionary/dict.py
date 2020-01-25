#LIbraries
import json
import difflib

#### Constants
dic = json.load(open("data.json"))

##### Function

# String, Dictionary -> String
# return the defination of the input word from the dictionary
def find_word_in_dictionary(word, dic):
    word = word.lower()
    if word in dic:
       array_definations = dic[word]
       print array_to_string(array_definations)
    else:
       check_similar_word(word, dic)


# Array -> String
# Takes the array and return the string of all the values concatenated to each other
def array_to_string(array_definations):
    return "/n".join(array_definations)


# String, Dictionary -> String
# Finds Similar words in Dictionary to a given word
def check_similar_word(word, dic, cutoff=0.5):
    result = []
    for key, value in dic.iteritems():
        sim = difflib.SequenceMatcher(None, word, key).ratio()
        if sim >= cutoff:
           result.append((sim, key))
    result.sort(key=lambda tup: tup[0])
    # find number of values to pick in the array

    if len(result)*.1 >3:
        num=3
    else:
        num = round(len(result)*.1)

    # Print the result
    if len(result) > 0:
        res= result[-3:]
        print "Did you mean", " or ".join([x[1] for x in res])
    else:
        print "No words found"
        # create an


# input from the user
def get_input():
    word = raw_input("Name of the word for which you want the defination")
    find_word_in_dictionary(word, dic)


get_input()

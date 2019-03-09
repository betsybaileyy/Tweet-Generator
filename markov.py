from dictogram import Dictogram
from sample import weighted_random, histogram
import random
import sys

# with open('tyra-banks-rant.txt') as f:
#     # setting the words variable and telling it to read the words and split them
#     words = f.read().split()

word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

''' BIG shoutout to Ansel for helping me with this function. THANK YOU ANSEL!! '''
def markov_markov(word_list): #takes in the word_list

    new_exciting_dictogram = {} #creating the new dictogram variable, set as empty (obviously)

    for index in range(len(word_list) - 1):
        word = word_list[index]
        next_word = word_list[index + 1]

        if word not in new_exciting_dictogram:
            add_word = Dictogram([next_word])
            new_exciting_dictogram[word] = add_word
        else:
            new_exciting_dictogram[word].add_count(next_word)

    return new_exciting_dictogram #dictionary


def get_next_word(new_exciting_dictogram, word):
    inner_dictionary = new_exciting_dictogram[word]
    next_random_word = weighted_random(inner_dictionary)
    return next_random_word

'''Thank you for helping me understand this soooo much better, Phyllis! Thank you to Stephanie, too :)'''
def generate_sentences(new_exciting_dictogram):
    first_word = list(new_exciting_dictogram.keys())[0]
    second_word = get_next_word(new_exciting_dictogram, first_word)
    phrase = first_word + ' ' + second_word + ' '

    previous_word = second_word

    for word in range(0, random.randint(1,101)):
        new_word = get_next_word(new_exciting_dictogram, previous_word)
        previous_word = new_word
        phrase += new_word + ' '
    return phrase




# print("next word dict : " + (str(next_word_dict)))

# pass in markov to generate generate_sentenc
#     set wordslist as an empty ARRAY
#     first_word = weighted_random
#     append first word to words lists
#         look into the markov of "following words" for first_word
#         use weighted random to choose a word from "following words" (what is real code for "following words")
#         to be next_word
#          append next word to the sentence
#        set first word equal to next word
#

# f.read(tyra_banks_rant.txt)
#     # setting the words variable and telling it to read the words and split them
# words = f.read().split()
    # taking in the number of words in sentence as a command line argument
    # number_of_words = int(sys.argv[1])

    # setting the sentence as an array
    # sentence = []

    # making a for loop to iterate through the list of words _ number of times
    # for i in range(number_of_words):
    #     random_word = random.choice(words)
    #     sentence.append(random_word)

    # formatting the output with capitilization and punctuation to create a cohesive sentence
    # grammar = ' '.join(sentence) + ('.')
    # proper_grammar = grammar.capitalize()

if __name__ == "__main__":
    sentence = markov_markov(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    # print(sentence)
    print(get_next_word(sentence, 'fish'))
    print(generate_sentences(sentence))
    # print(second_order(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'end']))




# def generate_sentence(markov_markov):
#     print("markov model: {}".format(markov_model))
#     sentence = []
#     first_word = weighted_random(markov_model)
#     print('first word: {}'.format(first_word))
#     sentence.append(first_word)
#     print('sentence: {}'.format(sentence))
#     next_dict = markov_markov[first_word]
#     # for key, value in markov_markov.keys(first_word)
#     #     next_word = weighted_random(first_word)
#     #     sentence.append(next_word)
#     #
#     #     first_word = next_word
#     print('first word: {}'.format(next_dict))
#     # return next_dict
#
# generate_sentence(markov_markov)




# def generate_sentence(new_exciting_dictogram):
#     # first_word = next_word_dict.keys()[0]
#     first_word = next_word_dict.keys()
#     second_word = next_word(next_word_dict, first_word)
#     phrase = first_word + ' ' + second_word + ' '
#
#     random_number = 20
#     previous_word = second_word
#
#     for word in range(random_word):
#         new_word = next_word(next_word_dict, previous_word)
#         previous_word = new_word
#         phrase += new_word + " "
#     return phrase
#
# print(generate_sentence(next_word_dict))

#
# # write a function that structures how to make a sentence
# # in that function for each part of the sentence, specify how it should use a markov chain to choose a word for each part of the
#
# choose the first word in the sentence
# def
#
# store each word in an array
#
# look at last word in array = left_word #this is the key inthe markov chain
#     this key will return a dictionary
#
# select one of the keys from that dictinary as the right_word
#     add this to the array, it will become the new left_word
#
# '''I owe many thanks to Ansel for next_word too'''

# def next_word(next_word_dict, previous_word):
#     next_word = next_word_dict[previous_word]
#     after_word = weighted_random(next_word)
#
#     return after_word
#
#
# next_word(next_word_dict, "fish")
#
# print(next_word(next_word_dict, "fish"))


from dictogram import Dictogram # bc my code is modular we can reuse the Dictogram class :) ygg

word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

'''
BIG shoutout to Ansel for helping me with this function. THANK YOU ANSEL!!
'''
def markov_markov(word_list): #takes in the word_list

    new_exciting_dictogram = {} #creating the new dictogram variable, set as empty (obviously)
    # test comment
    for index in range(len(word_list) - 1):
        word = word_list[index]
        next_word = word_list[index + 1]

        if word not in new_exciting_dictogram:
            add_word = Dictogram([next_word])
            new_exciting_dictogram[word] = add_word
        else:
            new_exciting_dictogram[word].add_count(next_word)

    return new_exciting_dictogram

print(markov_markov(word_list))

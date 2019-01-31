import random
import sys

# opening the file of english words on the Mac OS
with open('/usr/share/dict/words') as f:
    # setting the words variable and telling it to read the words and split them
    words = f.read().split()
    # taking in the number of words in sentence as a command line argument
    number_of_words = int(sys.argv[1])

    # setting the sentence as an array
    sentence = []

    # making a for loop to iterate through the list of words _ number of times
    for i in range(number_of_words):
        random_word = random.choice(words)
        sentence.append(random_word)

    # formatting the output with capitilization and punctuation to create a cohesive sentence
    grammar = ' '.join(sentence) + ('.')
    proper_grammar = grammar.capitalize()

    print(proper_grammar)

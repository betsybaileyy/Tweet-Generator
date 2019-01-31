import random
import sys


with open('/usr/share/dict/words') as f:

    words = f.read().split()

    number_of_words = int(sys.argv[1])


    sentence = []

    for i in range(number_of_words):
        random_word = random.choice(words)
        sentence.append(random_word)

    grammar = ' '.join(sentence) + ('.')
    proper_grammar = grammar.capitalize()

    print(proper_grammar)

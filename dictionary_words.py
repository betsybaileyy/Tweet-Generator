import random


f = open('/usr/share/dict/words', 'r')

words = f.read().split()

number_of_words = int(5)

sentence = []

for i in range(number_of_words):
    random_word = random.choice(words)
    sentence.append(random_word)

grammar = ' '.join(sentence) + ('.')
proper_grammar = grammar.capitalize()

print(grammar)

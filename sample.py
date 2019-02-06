from histogram import dictionary
import random

histogram = dictionary('hello world good day day day')

keys = histogram.keys()

word_list = list(keys)

random_index = random.randint(0, len(keys)-1)

random_word = word_list[random_index]

print(random_word)

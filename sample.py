from histogram import dictionary
from dictogram import Dictogram
import random



# TODO: perhaps name the dictionary method, histogram because dictionary means
# something different
_list = 'one fish two fish red fish blue fish'.split(' ')
histogram = Dictogram(_list)
# print('Histogram: {}'.format(histogram))

'''
Justin helped me map out and understand how to create
this get_random_word function. Thank you, Justin!!!
'''
def get_random_word(histogram):

    keys = histogram.keys()
    # print('Keys: {}'.format(keys))
    word_list = list(keys)
    random_index = random.randint(0, len(keys)-1)
    random_word = word_list[random_index]

    return random_word

# Getting a random word taking into account the frequency
# of that word, which will affect the likelyhood of that
# word being chosen.
def weighted_random(histogram):
    # Declaring tokens (total number of word occurences)
    tokens = 0
    # Setting the cumulative probobility
    # (numerical liklieness of a word being chosen) to zero.
    cumulative_prob = 0.0

    # Going through each key-value pair of words and frequencys (stored as a list)
    # in a list and adding each value at index number 1 (the frequency of that word)
    # to create a total sum, which will be the total number of tokens.
    for word, frequency in histogram.items():
        # print(type(histogram))
        # print(word)
        tokens += frequency

    # Random.uniform will return us a float between 0 and 0.99 that we will then
    # use to compare to the cumulative probability. If the cumulative_prob(ability)
    # is larger than the random number we will choose the string at index number 0
    # of the key-value pair (the word), if not, we will continue onto the next
    # key value pair until the cumulative_prob is larger than the random number,
    random_number = random.uniform(0,1)

    for word, frequency in histogram.items():
        cumulative_prob += frequency/tokens

        if cumulative_prob >= random_number:
            return word



print(weighted_random(histogram))

def rand_test(histogram):
    # for (let i = 0; i < 10000; i+=1) {}
    new_histogram = {}
    counter = 1000000 #0000
    new_list = []
    while counter:
        random_word = weighted_random(histogram)
        new_list.append(random_word)
        counter -= 1
    return dictionary(new_list)

print(rand_test(histogram))













# def frequency(histogram):
#     keys = histogram.keys()
#     # print('Keys: {}'.format(keys))
#     word_list = list(keys)
#     count = 0
#     # dictionary = histogram(histogram)
#     for key in histogram:
#         count += histogram[key]
#     rand = random.randrange(count)
#     num_total = 0
#     for key in histogram:
#         num_total += histogram[key]
#         if rand < num_total:
#             return key

# def frequency(histogram):
#     pass

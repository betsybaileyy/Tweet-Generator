from histogram import histogram
import random

# TODO: perhaps name the dictionary method, histogram because dictionary means
# something different
_list = 'one fish two fish red fish blue fish'.split(' ')
fish_o_gram = histogram(_list)
# print('Histogram: {}'.format(histogram))

'''
Justin helped me map out and understand how to create this get_random_word function. Thank you, Justin!!!
'''
def get_random_word(histogram):

    keys = histogram.keys()
    # print('Keys: {}'.format(keys))
    word_list = list(keys)
    random_index = random.randint(0, len(keys)-1)
    random_word = word_list[random_index]

    return random_word

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

def frequency(histogram):
    pass

print(frequency(fish_o_gram))

def rand_test(histogram):
    # for (let i = 0; i < 10000; i+=1) {}
    new_histogram = {}
    counter = 10000
    new_list = []
    while counter:
        random_word = get_random_word(fish_o_gram)
        new_list.append(random_word)
        counter -= 1
    return histogram(new_list)

print(rand_test(histogram))

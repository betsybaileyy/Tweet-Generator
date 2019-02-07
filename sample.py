from histogram import dictionary
import random

# TODO: perhaps name the dictionary method, histogram because dictionary means
# something different
_list = 'one fish two fish red fish blue fish'.split(' ')
histogram = dictionary(_list)
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

# print(get_random_word(histogram))

def rand_test(histogram):
    # for (let i = 0; i < 10000; i+=1) {}
    new_histogram = {}
    counter = 10000
    new_list = []
    while counter:
        random_word = get_random_word(histogram)
        new_list.append(random_word)
        counter -= 1
    return dictionary(new_list)

print(rand_test(histogram))

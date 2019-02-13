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

    return

def frequency(histogram):
    keys = histogram.keys()
    # print('Keys: {}'.format(keys))
    word_list = list(keys)
    count = 0
    dictionary = histogram(histogram)
    for key in dictionary:
        count += dictionary[key]
    rand = random.randrange(count)
    num_total = 0
    for key in dic:
        num_total += dictionary[key]
        if rand < num_total:
            return key

print(frequency(histogram))

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

# print(rand_test(histogram))

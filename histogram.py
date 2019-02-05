
seuss_txt = "one fish two fish red fish blue fish"

# cannot use sort or shuffle
# random()-> 0=<x<1 and uniform(a,b)

# 1. histogram() function that takes text and stores each
# word along with the frequency of that word
# WHAT IS THE MOST/LEAST FREQUENT WORD?

def word_frequency(seuss_txt):
    words_list = seuss_txt.split(" ")
    new_list = []
    for word in words_list:
        word_found = False
        if len(new_list) == 0:
            new_list.append([word, 1])
        else:
            for this_word in new_list:
                if word in this_word[0]:
                    word_found = True
                    this_word[1] += 1
                if not word_found:
                    new_list.append([word, 1])
    # print(new_list)
    # return new_list

word_frequency(seuss_txt)


# 2. unique_words() takes histogram() argument and returns the total
# number of unique words in a the histogram
# HOW MANY DIFFERENT WORDS ARE USED?

def dictionary(seuss_txt):
    words_list = seuss_txt.split()
    table = dict()
    for i in words_list:
        table[i] = table.get(i, 0) + 1
    # print(table)
    # return table

dictionary(seuss_txt)

# def unique_words(word_frequency):
#     counter = 0
#     for k, v in word_frequency.items():
#         if word_frequency[k] is 1:
#             counter += 1
#     print(counter)
#
# histogram = word_frequency(seuss_txt)
# print(unique_words(histogram))

# print(unique_words(seuss_txt))

word_list = [word for word in seuss_txt.split()]

# def touple(seuss_txt):
#
# below pair-programmed with KJ
# stored as key value pairs
def check(word_list, text):
    # count = 0
    new_list = []
    # print(word_list)
    # print(text)
    for word in word_list:
        count = 0
        for t in word_list:

            if word == t:
                count += 1
        wtuple = (word, count)
        new_list.append(wtuple)
    return new_list

    # print(count)

    # add to list inside of function then return that list

print(check(word_list, seuss_txt))

# stored as touples
# def check(word_list, text):
#     # count = 0
#
#     for word in word_list:
#         count = 0
#         for t in text:
#             if word == t:
#                 count += 1
#         wtuple = [t, count]
#         return wtuple
#
#     print(count)
#
# check(word_list, seuss_txt)


# if __name__ = '__main__':
#     betsy  = input("input first")
#     betsy2  = input("input second")
#     kj = (betsy, betsy2)
#     print(kj)

# 3. frequency() function that takes a word and histogram argument and
# returns the number of times a word appears in a text
# WHAT IS THE AVERAGE FREQUENCY OF EACH WORD IN THE TEXT?

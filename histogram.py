
seuss = "one fish two fish red fish blue fish"

# cannot use sort or shuffle
# random()-> 0=<x<1 and uniform(a,b)

# 1. histogram() function that takes text and stores each
# word along with the frequency of that word
# WHAT IS THE MOST/LEAST FREQUENT WORD?

def word_frequency(seuss):
    words_list = seuss.split(" ")
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
                    break
            if not word_found:
                new_list.append([word, 1])
    print(new_list)

word_frequency(seuss)


# 2. unique_words() takes histogram() argument and returns the total
# number of unique words in a the histogram
# HOW MANY DIFFERENT WORDS ARE USED?

# def unique_words(word_frequency):
#     counter = 0
#     for g in word_frequency.items():
#         if word_frequency[g] is 1:
#             counter += 1
#     return counter
#
# print(unique_words(seuss))


# 3. frequency() function that takes a word and histogram argument and
# returns the number of times a word appears in a text
# WHAT IS THE AVERAGE FREQUENCY OF EACH WORD IN THE TEXT?

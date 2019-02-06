
seuss_txt = "one fish two fish red fish blue fish red two"

# random()-> 0=<x<1 and uniform(a,b)

# 1. histogram() function that takes text and stores each
# word along with the frequency of that word
# WHAT IS THE MOST/LEAST FREQUENT WORD?

# As a LIST OF LISTS

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
    print(new_list)
    return new_list

word_frequency(seuss_txt)

# 2. unique_words() takes histogram() argument and returns the total
# number of unique words in a the histogram
# HOW MANY DIFFERENT WORDS ARE USED?

# As a DICTIONARY

def dictionary(seuss_txt):
    words_list = seuss_txt.split()
    table = dict()
    for i in words_list:
        table[i] = table.get(i, 0) + 1
    print(table)
    return table

dictionary(seuss_txt)



# As a TUPLE
word_list = [word for word in seuss_txt.split()]

def tuple_o_gram(word_list, text):
    count = 0
    list_of_tpls = []

    for word in word_list:
        in_list = False
        # count = 0
        # we haven't put anythng in there yet
        if len(list_of_tpls) == 0:
            list_of_tpls.append((word, 1))
        else:
            # look in list of tuples for word
            for tpl in list_of_tpls:
                # it was found
                if word == tpl[0] and not in_list:
                    in_list = True
                    count = tpl[1] + 1
                    list_of_tpls.remove(tpl)
                    print(list_of_tpls)
                    list_of_tpls.append((word, count))
                    print(list_of_tpls)

                # if was not found
            if not in_list:
                list_of_tpls.append((word, 1))
                # in_list = False


print(tuple_o_gram(word_list, seuss_txt))

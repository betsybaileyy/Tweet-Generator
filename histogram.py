

'''
TODO: Update this so it takes in an external text file and doesn't only use Dr.Seuss material
'''

# As a LIST OF LISTS
def word_frequency(world_list):
    new_list = []
    for word in word_list:
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
    return new_list

# As a DICTIONARY

def dictionary(word_list):
    table = dict()
    for i in word_list:
        table[i] = table.get(i, 0) + 1
    # print(table)
    return table

# TO DO: refactor this code so that when it prints to the console it only does so once.
# As a TUPLE
'''
Phyllis helped me with this function and my understanding of it SO MUCH!! Thank you, Phyllis!
'''
# word_list = [word for word in seuss_txt.split()]

def tuple_o_gram(word_list):
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
                    # print(list_of_tpls)
                    list_of_tpls.append((word, count))
                    # print(list_of_tpls)

                # if was not found
            if not in_list:
                list_of_tpls.append((word, 1))
                # in_list = False
    return list_of_tpls

if __name__ == "__main__":
    seuss_txt = "one fish two fish red fish blue fish"
    word_list = seuss_txt.split()
    print("1.) As a LIST OF LISTS:")
    print(word_frequency(word_list))
    print("2.) As a DICTIONARY:")
    print(dictionary(word_list))
    print("3.) As a TUPLE:")
    print(tuple_o_gram(word_list))

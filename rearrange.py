import random, sys

def shuffle_words(sys):
    # taking sentence from command line and rearragning it

    sys.argv.pop(0)

    sentence = []

    while len(sys.argv) > 0:
        chosen = random.choice(sys.argv)
        sentence.append(chosen)
        sys.argv.remove(chosen)
    return sentence

# def reverse(sys):
#     sys.argv.pop(0)
#
#     input = sys.argv
#
#     reverse_sentence = []
# 
#     for word in input:
#         reverse_sentence.insert(0, word)
#     return ' '.join(reverse_sentence)

if __name__ == '__main__':
    params = sys.argv
    print(shuffle_words(sys))
    # print(reverse(sys))

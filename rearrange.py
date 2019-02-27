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

if __name__ == '__main__':
    params = sys.argv
    print(shuffle_words(sys))

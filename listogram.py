from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        found = False #setting found to False
        self.tokens += count #tokens are the count pretty much


        for item in self: #loop through every word in the array
            if item[0] == word: # if the item at index 0 of the key value pair equals the word
                item[1] += count # add the item at index 1 to the count (frequency)
                found = True

        if not found: #if found not true then
            self.types += 1 #add another type
            self.append([word, count]) #add to the dictionary

        return

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""

        for item in self: #creating a for loop to iterate thrugh all all
            if item[0] == word: # if the item at index 0 of the key value pair equals the word
                return item[1]
        return 0



    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        found = False
        for item in self:
            if word == item[0]:
                return True
        if found == False:
            return False


    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""

        for i in rang(len(self)):
            if self[i][0] == target:
                return i
        return None


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()

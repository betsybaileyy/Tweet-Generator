from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n) Because every item in every bucket gets looped through to append new item"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) we are looping through all of the buckets to append values to an array"""
        # TODO: Loop through all buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values
        # TODO: Collect all values in each bucket

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) retrieves the key value pairs at each entry in all buckets(NOT SURE ABT THIS ONE)"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) has to loop through each bucket in the bucket array"""
        length = 0
        pair = []
        # TODO: Loop through all buckets
        for bucket in self.buckets:
            length += bucket.length()
        return length


        # TODO: Count number of key-value entries in each bucket

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(n) trying to determine if the bucket conatins the given key"""

        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index] #THIS IS AN ARRAY!
        entry = bucket.find(lambda key_value: key_value[0] == key)

        # Examine the entry that was returned - is it none?
        if entry is None:
            return False
        else:
            return True

        # return (entry is not None) - another way to write it
        # TODO: Check if key-value entry exists in bucket

    def get(self, key): # coded in class
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(n) trying to determine if the bucket conatins the given key"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)] #0(1) to calculate index

        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)

        # If found, return value associated with given key
        if entry is not None: # found entry
            return entry[1] # get the value only

        # Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))


    def set(self, key, value): # coded in class
        """Insert or update the given key with its associated value.
        TODO: Running time: O(n) because we search through every value until we find one that matches, delete it, then append the new entry"""
        # find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        entry = bucket.find(lambda key_value: key_value[0] == key)

        if entry:
            bucket.delete(entry)

        entry = (key, value)
        bucket.append(entry)


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(n) because we look into every bucket to determine wether or not the value is there until we find it"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        value = self.get(key)
        tuple = (key, value)
        # Check if key-value entry exists in bucket
        tuple_exist = self.contains(key)
        # If found, delete entry associated with given key
        if tuple_exist is True:
            bucket.delete(tuple)
        else: #Otherwise, raise error to tell user delete failed
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()

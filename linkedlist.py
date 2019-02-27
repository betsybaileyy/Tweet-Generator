class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty. O(1)"""
        return self.head is None

    def length(self):
        """TODO: Running time: O(n) Bc we have to iterate over all nodes
        and count one for each?"""
        #setting the counter at 0 and defining node
        count = 0
        node = self.head
        # looping through each node (while true) add to the node count
        while node !=None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Bc We are only changing the tail node"""

        new_node = Node(item)

        # if list is empty, make this node the head
        if self.tail is None:
            self.head = new_node # makes both the head and tail the new node(beacuse there is only one node)
            self.tail = new_node
        else:
            self.tail.next = new_node # the new node is added as the tail
            self.tail = new_node # tail is new node

        return new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Because we only change the first
        node and do not loop through all nodes."""

        # this new node
        new_node = Node(item)

        # if the list is empty make this new node both the head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: # set the next node to the head
            new_node.next = self.head
            self.head = new_node #make the new node the head


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) If item is near the head of the list.
        TODO: Worst case running time: O(n) if item is near the tail of the list
        or not present and we need to loop through all n nodes in the list.
        (We did the O Notation for this in class)"""
        # set the node as the head node
        node = self.head
        while node is not None: # for every node that exists
            if quality(node.data): # is the content (quality) is the same as data in the node
                return node.data # return the node that has matching data
            else: # otherwise
                node = node.next # transfer to the next node (and examine it)
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Only checking one entry (the head)
        TODO: Worst case running time: O(n) will look through entire linked list"""
        current_node = self.head
        previous_node = None
        found = False

        while current_node:
            if self.head.data == item:
                if self.head.next is not None:
                    self.head = self.head.next
                    found = True
                    break
                else:
                    self.head = None
                    self.tail = None
                    found = True
                    break
            elif current_node.data == item:
                if current_node == self.tail:
                    previous_node.next = None
                    self.tail = previous_node
                    found = True
                    break
                else:
                    previous_node.next = current_node.next
                    found = True
                    break
            else:
                previous_node = current_node
                current_node = current_node.next

        if not found:
            raise ValueError('Item not found: {}'.format(item))



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

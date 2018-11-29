#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=[]):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
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
        """Return a boolean indicating whether this linked list is empty."""
        return self.size == 0

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        newNode = Node(item)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
           Best case running time: O(0) If head has the quality.
           Worst case running time: O(size) If tail has the quality"""
        curr = self.head
        while curr:
            if quality(curr.data):
                return curr.data
            curr = curr.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
           Best case running time: O(0) If head has the quality.
           Worst case running time: O(size) If tail has the quality"""
        prev = None
        curr = self.head
        while curr:
            if curr.data == item:
                if prev == None:
                    self.head = self.head.next
                else:
                    prev.next = curr.next
                    if prev.next is None:
                        self.tail = prev
                # Thank you Dylan Finn for the following if statement
                if self.tail is not None and self.tail.data is item:
                    self.tail = None
                self.size -= 1
                return
            prev = curr
            curr = curr.next
        raise ValueError("Couldn't find item in list.")


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

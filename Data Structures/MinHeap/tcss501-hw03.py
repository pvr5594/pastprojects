"""Credit: https://gist.github.com/nichochar/9664b184ae1a191eed75 The code from this link was instrumental in
implementing this MinHeap. Thanks to Kevin Perkins for showing me this link. """

from collections import deque
from random import randint


class MinHeap:
    class HeapNode:
        def __init__(self, data, parent=None):
            self.data = data
            self.parent = parent
            self.left = None
            self.right = None

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.root = None
        self.size = 0

    def findNode(self):
        curr = self.root

        if curr.left is None and curr.right is None:
            return curr

        while curr.left or curr.right:
            if curr.left is not None:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def bubbleUp(self, node):
        if node.parent is None:
            return
        if node.parent.data > node.data:
            node.data, node.parent.data = node.parent.data, node.data
            self.bubbleUp(node.parent)
        return

    def bubbleDown(self, node):
        if node.right and node.data > node.right.data:
            node.data, node.right.data = node.right.data, node.data
            return self.bubbleDown(node.right)
        if node.left and node.data > node.left.data:
            node.data, node.left.data = node.left.data, node.data
            return self.bubbleDown(node.left)
        if node.left is None and node.right is None:
            if node.parent.left.data < node.parent.data:
                self.bubbleUp(node.parent.data)
            elif node.parent.right.data < node.parent.data:
                self.bubbleUp(node.parent.data)
        return

    def heapSize(self):
        return self.size

    def insert(self, data):
        """
        Insert the provided data onto the heap. Should support integers and strings at least.
        Must be implemented with no worse than O(log n) time complexity.
        """
        n = MinHeap.HeapNode(data)
        if self.root is None:
            self.root = n
            self.size += 1

        else:
            node = self.findNode()
            new_node = MinHeap.HeapNode(data, node)
            if node.parent is None:
                if node.left is None:
                    node.left = new_node
                    self.bubbleUp(new_node)
                elif node.right is None:
                    node.right = new_node
                    self.bubbleUp(new_node)
            else:
                if node.left is None:
                    node.left = new_node
                    self.bubbleUp(new_node)
                elif node.right is None:
                    node.right = new_node
                    self.bubbleUp(new_node)
            self.size += 1
        return

    def pop(self):
        """
        Returns and removes the minimum value from the heap. If the heap is empty, return None.
        Must be implemented with no worse than O(log n) time complexity.
        """
        if self.root is None:
            return None
        else:
            curr = self.root
            node_data = self.root.data
            if curr.left:
                child = curr.left
            else:
                child = curr.right
            self.root = child
            self.size -= 1
            if self.root is not None:
                self.bubbleDown(self.root)
            return node_data

    def peek(self):
        """
        Return but do not remove the minimum value of the heap. If the heap is empty, return None.
        Must be implemented with no worse than O(1) time complexity.
        """
        if self.root is None:
            return None
        else:
            return self.root.data

    def clear(self):
        """
        Removes all elements from the heap. Must be implemented in no worse than O(1) time.
        """
        self.root = None
        return self.root

    def __repr__(self):
        if self.root is None:
            return ''
        else:
            queue = deque([self.root])
            results = []
            while len(queue) > 0:
                current = queue.pop()
                if current is None:
                    continue
                else:
                    results.append(current.data)
                if current.left is not None:
                    queue.appendleft(current.left)
                if current.right is not None:
                    queue.appendleft(current.right)

        return ' '.join([str(result) for result in results])


def test():
    print('MinHeap')
    t = MinHeap()

    t.peek()
    t.pop()
    t.insert(10)
    print('Made basic heap with 1 element, printing it')
    print(t)
    t.peek()
    t.pop()
    t.peek()
    print(t)
    t.clear()

    print('\nAdding a bunch of numbers and printing it again')
    t.insert(3)
    t.insert(7)
    t.insert(5)
    t.insert(2)
    t.insert(8)
    t.insert(10)
    print(t)
    t.peek()
    t.pop()
    t.peek()
    print(t)
    t.clear()

    print('\nAdding random numbers')
    for i in range(10):
        rand = randint(10, 100)
        t.insert(rand)
    print(t)
    t.peek()
    t.pop()
    t.peek()
    print(t)
    t.clear()

    print('\nAdding a bunch of characters and printing it again')
    t.insert('d')
    t.insert('j')
    t.insert('!')
    t.insert('2')
    t.insert('.')
    t.insert('?')
    print(t)
    t.peek()
    t.pop()
    t.peek()
    print(t)
    t.clear()

    print('\nAdding a bunch of strings and printing')
    t.insert('Hello')
    t.insert('World')
    t.insert('My')
    t.insert('Name')
    t.insert('Is')
    t.insert('Pranav')
    print(t)
    t.peek()
    t.pop()
    t.peek()
    print(t)
    t.clear()


if __name__ == '__main__':
    test()

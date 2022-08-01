class LinkedList:
    class ListNode:
        def __init__(self, data=None):
            self.next = None
            self.prev = None
            self.data = data

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
        self.char_count = 0

    def append(self, data):
        n = LinkedList.ListNode(data)

        if self.first is None:
            self.first = n
            self.last = n
            self.char_count = len(data)
        else:
            n.prev = self.last
            self.last.next = n
            self.last = n
            self.char_count = self.char_count + len(data)

        self.count += 1

    def revAppend(self, data):
        n = LinkedList.ListNode(data)
        if self.first is None:
            self.first = n
            self.last = n
        else:
            n.next = self.first
            self.first.prev = n
            self.first = n

    def size(self):
        return self.count

    def iter(self):
        curr = self.first
        while curr:
            ret = curr.data
            curr = curr.next
            yield ret

    def delete(self, data):
        curr = self.first
        deleted_fl = False

        if curr is None:
            deleted_fl = False
        elif curr.data == data:
            if self.first == self.last:
                self.last = None
            self.first = curr.next
            deleted_fl = True
        elif self.last.data == data:
            self.last = self.last.prev
            self.last.next = None
            deleted_fl = True
        else:
            while curr:
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    deleted_fl = True
                curr = curr.next

        if deleted_fl:
            self.count -= 1
            self.char_count = self.char_count - len(data)

    def contains(self, data):
        for n in self.iter():
            if data == n:
                return True
            return False

    def search(self, data):
        curr = self.first
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def clear(self):
        self.first = None
        self.last = None

    def charCount(self, aggregated=False):
        """
        Returns the total number of characters contained in the nodes of the linked list.
        If the `aggregated' argument is True, the result should be a single integer
        representing the sum of character counts of all elements in the LinkedList.  If False,
        the result should be a list of integers representing the count of characters of each
        node.  In both cases, if the list is empty, return `None'.  The aggregated version of
        this method should be O(1) and the dis-aggregated version should be O(n).

        :param aggregated: If True, aggregate the counts into a single value. If False, return
        a list of counts.
        :return: A single integer or list of integers as described above.
        """
        if self.first is None:
            return None
        curr = self.first
        if aggregated is False:
            count_list = []
            while curr:
                data = curr.data
                curr = curr.next
                count_list.append(len(data))
            return count_list
        if aggregated is True:
            return self.char_count

    def reverse(self, in_place=False):
        """
        Reverses the order of elements of the list, either in place (modifies the existing
        list) or replicates and returns a new copy of the list.  If in_place==True then
        modifications should be made to `self'. If in_place==False do not modify self, but
        rather create a new list and return the new list to the caller.  If the list is empty,
        in_place==True should do nothing, and in_place==False should return a new empty
        LinkedList.  Reverse should be no worse than O(n).

        :param in_place: If True, operations are performed on this instantiation of the List.
        Returns a new reversed version of the list otherwise.
        :return: If in_place == True, returns None, otherwise returns a new LinkedList object.
        """
        curr = self.first
        if in_place is True:
            prev = None
            while curr:
                while curr is not None:
                    nn = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nn
                self.first = prev
            return None
        if in_place is False:
            new_list = []
            while curr:
                new_list.append(curr.data)
                curr = curr.next
            self.first = None
            self.last = None
            new_linked_list = LinkedList
            for i in new_list:
                rev_data = i
                new_linked_list.revAppend(self, rev_data)
            new_linked_list.printList(self)
            return new_linked_list

    def printList(self):
        plist = self.first
        while plist:
            print(plist.data, end=" ")
            plist = plist.next
        print("\n")


class Deque:
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def addFirst(self, data):
        n = Deque.QueueNode(data)
        if self.bottom is None:
            self.top = n
            self.bottom = n
        else:
            self.top.next = n
            n.prev = self.top
            self.top = n
        self.size += 1

    def addLast(self, data):
        n = Deque.QueueNode(data)
        if self.top is None:
            self.top = n
            self.bottom = n
        else:
            self.bottom.prev = n
            n.next = self.bottom
            self.bottom = n
        self.size += 1

    def removeFirst(self):
        ret = self.top

        if self.size == 1:
            self.top = None
            self.bottom = None
        elif self.size > 1:
            self.top = self.top.prev
            self.top.next = None

        if self.size >= 1:
            self.size -= 1
            return ret.data

    def removeLast(self):
        ret = self.bottom

        if self.size == 1:
            self.top = None
            self.bottom = None
        elif self.size > 1:
            self.bottom = self.bottom.next
            self.bottom.prev = None

        if self.size >= 1:
            self.size -= 1
            return ret.data


def test():
    x = LinkedList()
    x.append("Hello")
    x.append("World")
    x.append("Goodbye")
    x.append("Everybody")
    x.printList()
    x.charCount()
    x.charCount(aggregated=True)
    x.reverse(in_place=True)
    x.printList()
    x.reverse(in_place=False)


if __name__ == '__main__':
    test()

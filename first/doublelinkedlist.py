class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        curr = self.head
        while curr is not None:
            if curr.value == val:
                return curr
            curr = curr.next
        return None

    def find_all(self, val):
        curr = self.head
        list_values = list()
        while curr is not None:
            if curr.value == val:
                list_values.append(curr)
            curr = curr.next
        return list_values

    def delete(self, val, all=False):
        pass

    def clean(self):
        pass

    def len(self):
        return 0

    def insert(self, afterNode, newNode):
        pass

    def add_in_head(self, newNode):
        pass

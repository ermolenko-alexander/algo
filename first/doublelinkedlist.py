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
        if self.head is None:
            return

        curr = self.head
        while curr is not None:
            if curr.value == val:
                if curr.prev is None:
                    if curr.next is None:
                        self.head = None
                        curr = None
                    else:
                        self.head = curr.next
                        self.head.prev = None
                        if not all:
                            break
                        curr = self.head
                else:
                    if curr.next is None:
                        self.tail = curr.prev
                        curr.prev.next = None
                        curr = None
                    else:
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                        curr = curr.prev
                        if not all:
                            break
            else:
                curr = curr.next

        if self.head is None:
            self.tail = None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        return 0

    def insert(self, afterNode, newNode):
        pass

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

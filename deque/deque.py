class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Deque:
    def __init__(self):
        self.deque = DoubleLinkedList()

    def addFront(self, item):
        node = Node(item)
        if self.deque.head is None:
            self.deque.tail = node
            node.next = None
            node.prev = None
        else:
            node.next = self.deque.head
            self.deque.head.prev = node
        self.deque.head = node

    def addTail(self, item):
        node = Node(item)
        if self.deque.head is None:
            self.deque.head = node
            node.next = None
            node.prev = None
        else:
            self.deque.tail.next = node
            node.prev = self.deque.tail
        self.deque.tail = node

    def removeFront(self):
        if self.deque.head is None:
            return None
        remove_value = self.deque.head.value
        self.deque.head = self.deque.head.next
        return remove_value

    def removeTail(self):
        if self.deque.head is None:
            return None

        remove_value = self.deque.tail.value
        if self.deque.head == self.deque.tail:
            self.deque.head = None
            self.deque.tail = None
            return remove_value

        self.deque.tail = self.deque.tail.prev
        self.deque.tail.next = None
        return remove_value

    def size(self):
        node = self.deque.head
        len_deque = 0
        while node:
            len_deque += 1
            node = node.next
        return len_deque

class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


class Queue:

    def __init__(self):
        self.queue = LinkedList()

    def size(self):
        if self.queue.head is None:
            return 0

        curr = self.queue.head
        len_queue = 0
        while curr is not None:
            len_queue += 1
            curr = curr.next
        return len_queue

    def enqueue(self, item):
        en_node = Node(item)
        if self.queue.head is None:
            self.queue.head = en_node
        else:
            self.queue.tail.next = en_node
        self.queue.tail = en_node

    def dequeue(self):
        if self.queue.head:
            deq_value = self.queue.head.value
            self.queue.head = self.queue.head.next
            return deq_value
        return None

    
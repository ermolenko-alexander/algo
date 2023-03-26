class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList2:

    def __init__(self):
        self.head = None
        self.tail = None


class Stack:
    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        curr = self.stack.head
        len_stack = 0

        while curr is not None:
            len_stack += 1
            curr = curr.next
        return len_stack

    def pop(self):
        if self.stack.tail is None:
            return

        pop_value = self.stack.tail.value
        if self.stack.head == self.stack.tail:
            self.stack.tail = None
            self.stack.head = None
            return pop_value

        self.stack.tail = self.stack.tail.prev
        self.stack.tail.next = None

        return pop_value

    def push(self, value):
        push_node = Node(value)

        if self.stack.head is None:
            self.stack.head = push_node
            self.stack.head.prev = None
            self.stack.head.next = None
        else:
            self.stack.tail.next = push_node
            push_node.prev = self.stack.tail
        self.stack.tail = push_node

    def peek(self):
        if self.stack.tail is None:
            return None
        return self.stack.tail.value

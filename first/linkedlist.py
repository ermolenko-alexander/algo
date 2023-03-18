class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        val_nodes = list()
        curr = self.head

        while curr is not None:
            if curr.value == val:
                val_nodes.append(curr)
            curr = curr.next
        return val_nodes

    def delete(self, val, all=False):
        pre = None
        curr = self.head

        while curr is not None:
            if curr.value == val:
                if self.head is curr and self.tail is curr:
                    self.head = None
                    self.tail = None
                elif self.head is curr:
                    self.head = curr.next
                elif self.tail is curr:
                    self.tail = pre
                else:
                    pre.next = curr.next
                if not all:
                    break
            else:
                pre = curr
            curr = curr.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        list_len = 0
        node = self.head

        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, afterNode, newNode):
        curr = self.head

        if afterNode is None:
            if curr is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        elif afterNode is self.tail:
            self.add_in_tail(newNode)
        else:
            while curr is not None:
                if curr is afterNode:
                    newNode.next = curr.next
                    curr.next = newNode
                    break
                curr = curr.next
          

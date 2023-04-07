class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add(self, value):
        add_node = Node(value)

        if self.head is None:
            self.head = add_node
            self.tail = add_node
            return

        compare_head = self.compare(value, self.head.value)
        if compare_head <= 0 and self.__ascending or compare_head >= 0 and not self.__ascending:
            add_node.next = self.head
            self.head.prev = add_node
            self.head = add_node
            return

        compare_tail = self.compare(value, self.tail.value)
        if compare_tail >= 0 and self.__ascending or compare_tail <= 0 and not self.__ascending:
            self.tail.next = add_node
            add_node.prev = self.tail
            self.tail = add_node
            return

        curr = self.head.next
        while curr is not None:
            curr_compare = self.compare(value, curr.value)
            if curr_compare <= 0 and self.__ascending or curr_compare >= 0 and not self.__ascending:
                add_node.next = curr
                add_node.prev = curr.prev
                curr.prev.next = add_node
                curr.prev = add_node
                break
            curr = curr.next

    def find(self, val):
        curr = self.head

        while curr is not None:
            curr_compare = self.compare(val, curr.value)
            if curr_compare == 0:
                return curr
            if curr_compare < 0 and self.__ascending or curr_compare > 0 and not self.__ascending:
                break
            curr = curr.next
        return

    def delete(self, val):
        if self.head is None:
            return

        compare_head = self.compare(val, self.head.value)
        compare_tail = self.compare(val, self.tail.value)
        if compare_head < 0 and self.__ascending or compare_head > 0 and not self.__ascending:
            return
        if compare_tail > 0 and self.__ascending or compare_tail < 0 and not self.__ascending:
            return
        if compare_head == 0 and self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None
        elif compare_head == 0 and self.head.next is None:
            self.head = None
            self.tail = None
            return
        if compare_tail == 0:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        curr = self.head.next
        while curr is not None:
            curr_compare = self.compare(val, curr.value)
            if curr_compare == 0:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.prev = None
                curr.next = None
                break
            if curr_compare < 0 and self.__ascending or curr_compare > 0 and not self.__ascending:
                break
            curr = curr.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        len_list = 0
        node = self.head
        while node:
            len_list += 1
            node = node.next
        return len_list

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

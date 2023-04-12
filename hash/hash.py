class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(value.encode('utf-8')) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        accounting_index = []
        while True:
            accounting_index.append(index)
            if not self.slots[index]:
                return index

            index = (index + self.step) % self.size
            if len(accounting_index) == len(self.slots):
                return None

    def put(self, value):
        index = self.seek_slot(value)
        if index or index == 0:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        accounting_index = []
        index = self.hash_fun(value)
        while True:
            accounting_index.append(index)
            if self.slots[index] == value:
                return index

            index = (index + self.step) % self.size
            if len(accounting_index) == self.size:
                return None

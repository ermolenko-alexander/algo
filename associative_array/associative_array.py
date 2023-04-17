class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return sum(key.encode('utf-8')) % self.size

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        index = self.hash_fun(key)
        for i in range(self.size):
            if not self.slots[index] or self.slots[index] == key:
                self.slots[index] = key
                self.values[index] = value
                return
            index = (index + 4) % self.size

    def get(self, key):
        try:
            slot_index = self.slots.index(key)
            return self.values[slot_index]
        except ValueError:
            return

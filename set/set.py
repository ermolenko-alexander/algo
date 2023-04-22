class PowerSet:

    def __init__(self):
        self.cells = []

    def size(self):
        return len(self.cells)

    def put(self, value):
        if value not in self.cells:
            self.cells.append(value)
        return

    def get(self, value):
        if value in self.cells:
            return True
        return False

    def remove(self, value):
        try:
            self.cells.remove(value)
            return True
        except ValueError:
            return False

    def intersection(self, set2):
        set_inter = PowerSet()
        for value in self.cells:
            if set2.get(value):
                set_inter.put(value)
        return set_inter

    def union(self, set2):
        set_union = PowerSet()
        set_union.cells = self.cells.copy()
        for elem in set2.cells:
            if elem not in set_union.cells:
                set_union.put(elem)
        return set_union

    def difference(self, set2):
        set_diff = PowerSet()
        for value in self.cells:
            if value not in set2.cells:
                set_diff.put(value)
        return set_diff

    def issubset(self, set2):
        arr1 = self.cells.copy()
        arr2 = set2.cells.copy()

        return sorted(arr2) == sorted(arr1)[:len(arr2)]

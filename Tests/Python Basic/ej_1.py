class Multiset:
    data = set()
    
    def add(self, val):
        self.data.add(val)

    def remove(self, val):
        if val in self.data:
            self.data.remove(val)

    def __contains__(self, val):
        return True if val in self.data else False
    
    def __len__(self):
        return len(self.data)

m = Multiset()
m.add(2)
m.add(2)

print(m.data)

import random

class Item:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __repr__(self):
        return str(self.value)

class HashTable:
    def __init__(self,size,p=1009):
        self.size = size
        self._lst = [[] for x in range(self.size)]
        self.h = self._getHashFunction(p)

    def __getitem__(self,key):
        hkey = self.h(key)
        for elem in self._lst[hkey]:
            if elem.key == key:
                return elem.value

        raise IndexError

    def __setitem__(self,key,value):
        item = Item(key,value)
        hkey = self.h(key)
        for i in range(len(self._lst[hkey])):
            if self._lst[hkey][i].key == key:
                self._lst[hkey][i] = item
                return

        self._lst[hkey].append(item)

    def __repr__(self):
        return str(self._lst)

    def __len__(self):
        return sum(map(len,self._lst))

    def __contains__(self,key):
        hkey = self.h(key)
        for item in self._lst[hkey]:
            if item.key == key:
                return True

        return False

    def __delitem__(self,key):
        if not key in self:
            raise IndexError

        hkey = self.h(key)
        for i in range(len(self._lst[hkey])):
            if self._lst[hkey][i].key == key:
                del self._lst[hkey][i]
                return

    def _getHashFunction(self,p):
        a = random.randrange(1,p)
        b = random.randrange(p)
        def h(x):
            return ((a * x + b) % p) % self.size

        return h

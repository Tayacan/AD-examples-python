import random

class Item:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self,size,p=1009):
        self.size = size
        self._lst = [[] for x in range(self.size)]
        self.h = self._getHashFunction(p)

    def __getitem__(self,k):
        return self.get(k)

    def __setitem__(self,key,value):
        self.insert(key,value)

    def insert(self,key,value):
        item = Item(key,value)
        hkey = self.h(key)
        for i in range(len(self._lst[hkey])):
            if self._lst[hkey][i].key == key:
                self._lst[hkey][i] = item
                return

        self._lst[hkey].append(item)

    def get(self,key):
        hkey = self.h(key)
        for elem in self._lst[hkey]:
            if elem.key == key:
                return elem.value

        return None

    def _getHashFunction(self,p):
        a = random.randrange(1,p)
        b = random.randrange(p)
        def h(x):
            return ((a * x + b) % p) % self.size

        return h

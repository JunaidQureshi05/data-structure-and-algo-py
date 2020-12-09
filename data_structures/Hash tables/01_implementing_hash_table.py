# O(n) Space
# Time Complexity
# Best Case
# O(1) insert
# O(1) remove
# O(1) lookup
# Worst case - linked list formation(hash collisions)
# O(n) insert
# O(n) remove
# O(n) lookup

class HashTable:
    def __init__(self,size):
        self.buckets = size
        self.data = [[] for i in range(self.buckets)]

    def hash(self,key):
        hash = 0
        for  i in range(len(key)):
            hash =( hash + ord(key[i]) * i) % self.buckets
        return hash;

    def __str__(self):
        return str(self.__dict__)
    
    def set(self,key,value):
        hash_value = self.hash(key)
        reference = self.data[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][1] =value
                return None
        self.data[hash_value].append([key,value])
        return None        
    def get(self,key):
        hash_value = self.hash(key)
        reference = self.data[hash_value]
        for i in range(len(reference)):
            if self.data[hash_value][i][0] ==key:
                return self.data[hash_value][i][1]
        return None
    def remove(self,key):
        hash_value = self.hash(key)
        reference = self.data[hash_value]
        for i in range(len(reference)):
            if reference[i][0] ==key:
                reference.pop(i)
                return None
        return None
    def keys(self):
        keys_array = []
        for i in range(self.buckets):
            if(self.data[i]):
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0][0])                 
        return keys_array
fruits = HashTable(20)

fruits.set('orange',10)
fruits.set('banana',12)
fruits.set('apple',185)
fruits.set('mango',200)
fruits.set('kivi',2)
fruits.set('strawberry',2)
fruits.set('guava',12)
fruits.set('banana',313)
print(fruits.keys())     
# O(n) Space

# Time complexity
# Best case
# lookup - O(1)
# insert - O(n)
# delete - O(n)
# push - (1)

# Worst case
# lookup - O(1)
# insert - O(n)
# delete - O(n)
# append - (n)  - dynamic array

# Implementing array using python class

class Array:
  def __init__(self):
    self.length = 0
    self.data = {}

  def __str__(self):
    return str(self.__dict__)
  
  def push(self,item):  #)(1)
    self.data[self.length] = item
    self.length +=1
  def pop(self): #O(1)
    last_item =self.data [self.length-1]
    del self.data[self.length-1]
    self.length-=1
    return last_item
  def get(self,idx): #O(1)
    return self.data[idx]

  def delete(self,idx): #O(n)
    deleteditem = self.data[idx]
    for i in range(idx,self.length-1):
      self.data[i] = self.data[i+1]

    del self.data[self.length-1]
    self.length-=1
    return deleteditem


persons = Array()

persons.push('Junaid')
persons.push('Siyam')
persons.push('Anzar')

print(persons.delete(0))
print(persons.delete(0))
print(persons)
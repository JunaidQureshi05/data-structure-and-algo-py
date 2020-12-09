# O(n) Space

# Time coplexity

# O(1) Enqueue
# O(1) Dequeue

class Node:
    def __init__(self,value):
        self.value =value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def enqueue(self,value):
        node =Node(value)
        if self.first == None:
            self.first = node
            self.last = self.first
        else:
            self.last.next = node
            self.last = node
        self.length +=1
    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last= None    
        deleted_item = self.first
        self.first = self.first.next
        self.length -=1
        return deleted_item.value
    def print_queue(self):
        current = self.first
        while current is not None:
            print(current.value,end=" ")
            current = current.next
        if self.first:
            print({"length":self.length,"first":self.first.value,"last":self.last.value})
        else:
            print(None)
    def peek(self):
        if self.first ==None:
            return
        return self.first.value            
my_queue =Queue()
my_queue.enqueue('a')
my_queue.enqueue('b')
my_queue.enqueue('c')
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
my_queue.enqueue('Junaid')
my_queue.enqueue('Ahemad')
my_queue.enqueue('Qureshi')
my_queue.dequeue()
print(my_queue.peek())
my_queue.print_queue()
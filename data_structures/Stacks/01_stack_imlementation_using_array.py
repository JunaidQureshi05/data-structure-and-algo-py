# O(n) Space

# Time complexity
# O(1) -push
# O(1) -pop
# O(1) -peek


class Stack:
    def __init__(self):
        self.data = []
        self.length = 0

    def push(self,item):
        self.data.append(item)
        self.length +=1

    def pop(self):
        if self.length ==0:
            return
        deleted_item =self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return deleted_item     
    def peek(self):
        if self.length ==0:
            return 
        return self.data[self.length-1]

    def __str__(self):
        return str(self.__dict__)


my_stack = Stack()

my_stack.push('facebook')
my_stack.push('amazon')
my_stack.push('apple')
my_stack.push('alibaba')
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
print(my_stack)        
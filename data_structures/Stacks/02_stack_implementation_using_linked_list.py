# O(n) Space

# Time complexity
# O(1) -push
# O(1) -pop
# O(1) -peek


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        


class Stack:
    def __init__(self):
        self.top =None
        self.bottom =None
        self.length =0
    def push(self,item):
        node = Node(item)
        if self.bottom is None:
            self.bottom = node
            self.top = self.bottom
        else:
            node.next = self.top
            self.top= node
        self.length +=1    
    def peek(self):
        return self.top.value

    def pop(self):
        if not self.top:
            self.bottom = None
            return
        if self.top ==self.bottom:
            self.bottom =None    
        deleted_item = self.top
        self.top =self.top.next
        self.length -=1
        return deleted_item.value
    def print_stack(self):
        current =self.top
        items = []
        while current:
            items.append(current.value)
            current =current.next
        if self.top:    
            print( {"items":items,"top":self.top.value,"bottom":self.bottom.value,"length":self.length})
        else:
            print(None)    
my_list2 = Stack()
my_list2.push('Junaid')
my_list2.push('Hadiya')
print(my_list2.pop())
print(my_list2.pop())
my_list2.print_stack()

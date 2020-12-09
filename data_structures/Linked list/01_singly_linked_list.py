# O(n) Space
# Time complexity
# insert - O(1)
# delete - O(1)
# lookup - O(n)
# access - O(n)
# Time complexity (If traversing considerd )
# insert - O(n)
# delete - O(n)
# lookup - O(n)
# access - O(n)
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head =None
        self.tail =  None
        self.length=0
    def prepend(self,value):
        node =  Node(value)
        node.next = self.head
        self.head = node
        self.length +=1    
    def append(self,value):
        node = Node(value)
        if self.head ==None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length +=1
    def insert(self,idx,value):
        node =Node(value)
        if idx <=0:
            self.prepend(value)
        elif idx>= self.length-1:
            self.append(value)
        else:
            counter = 0
            leader = self.head
            while counter < idx:
                if counter == idx-1:
                    # follower = leader.next
                    # node.next =follower
                    # leader.next = node
                    # short hand
                    leader.next , node.next = node , leader.next 
                leader =leader.next
                counter+=1    

        self.length+=1                 
    def print_list(self):
        head = self.head
        while head is not None:
            print(head.value,end=' ')
            head = head.next
        return f"Length:- {self.length}"         
    def remove(self,idx):
        if idx >= self.length or idx < 0:
            print('Please enter a valid index')
        if idx == 0:
            self.head = self.head.next
            self.length-=1
        else:
            temp =self.head
            counter = 0
            while counter <idx:
                if counter == idx -1 :
                    temp.next =temp.next.next
                    self.length-=1 
                temp =temp.next
                counter+=1
    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node  = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node    
    def __str__(self):
        return str(self.__dict__)
        
my_list = LinkedList()
my_list.append('a') 
my_list.append('b')
my_list.append('c')  
my_list.append('d') 
my_list.append('e') 
my_list.append('f')
my_list.remove(3) 
my_list.insert(1,'Junaid')
print(my_list.print_list())
my_list.reverse()
my_list.print_list()

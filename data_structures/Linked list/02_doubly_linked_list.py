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
        self.prev = None
        self.next = None

class DoublyLiskedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length =0
    def append(self,value):
        node = Node(value)
        if self.head ==None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail  =node
        self.length+=1   
    def prepend(self,value):
        node =Node(value)
        node.next =self.head
        self.head.prev = node
        self.head = node
        self.length+=1
    def print_list(self):
        temp =self.head
        print('Length ',self.length)
        if self.length !=0:
            print('Head ',self.head.__dict__)
            print('Tail ',self.tail.__dict__)
        while temp !=None:
            print(temp.value,end = ' ')
            temp =temp.next       
    def insert(self,idx,value):
        if idx<= 0:
            self.prepend(value)
        elif idx>=self.length:
            self.append(value)
        else:    
            node = Node(value)
            counter = 0
            leader = self.traverse_to_index(idx-1)
            follower = leader.next
            node.next = follower
            follower.prev = node
            leader.next = node
            node .prev = leader
            self.length+=1
            counter +=1
    def remove(self,idx):
        if idx ==0:
            self.head = self.head.next
            self.head.prev =None
            self.length -=1
        elif idx == self.length-1:
            self.tail = self.tail.prev
            self.tail.next =None
            self.length -=1
        else:       
            leader = self.traverse_to_index(idx-1)
            follower = leader.next.next
            leader.next= follower
            follower.prev = leader                                 
    def traverse_to_index(self,idx):
        temp = self.head
        i=0
        while i != idx:
            temp = temp.next
            i+=1
        return temp         

new_list = DoublyLiskedList()
new_list.append("Junaid")
new_list.append("Qureshi")
new_list.prepend("Hadiya")
new_list.insert(1,1)
new_list.remove(1)
new_list.print_list()

        
class Node:
    def __init__(self,value):
        self.value =value
        self.right =None
        self.left =None



class BinarySearchTree:
    def __init__(self):
        self.root= None

    def insert(self,value):
        node =Node(value)
        if self.root ==None:
            self.root = node
            return
        else:
            currentNode =self.root
            while True:
                if currentNode.value < node.value:
                    if currentNode.right ==None:
                        currentNode.right =node
                        return
                    
                    currentNode =currentNode.right
                elif currentNode.value > node.value:
                    if currentNode.left ==None:
                        currentNode.left =node
                        return
                    currentNode = currentNode.left          
                else:
                    print('No duplication allowed')
                    break
    def lookup(self,value):
        currentNode = self.root
        while currentNode !=None:
            if currentNode.value < value:
                currentNode =currentNode.right
            elif currentNode.value > value:
                currentNode =currentNode.left
            else:
                return True
        return False      
    def remove(self,value):
        currentNode

    def breadth_first_search_(self):
        currentNode = self.root
        array = []
        queue = []
        queue.append(self.root)

        while(len(queue)>0):
            currentNode = queue[0]
            del queue[0]
            array.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)    
        return array
    def breadth_first_search_recursive(self,queue,array):
        if(not len(queue)):
            return array
        currentNode = queue[0]
        del queue[0]
        array.append(currentNode.value)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        return self.breadth_first_search_recursive(queue,array)             
my_bst=BinarySearchTree()

my_bst.insert(20)
my_bst.insert(10)
my_bst.insert(30)
my_bst.insert(5)
my_bst.insert(12)
my_bst.insert(25)
my_bst.insert(35)
my_bst.insert(3)
my_bst.insert(6)
my_bst.insert(11)
my_bst.insert(24)
my_bst.insert(13)

my_bst.insert(28)
my_bst.insert(32)
my_bst.insert(38)
# print(my_bst.lookup(4))
print(my_bst.breadth_first_search_())
print(my_bst.breadth_first_search_recursive([my_bst.root],[]))
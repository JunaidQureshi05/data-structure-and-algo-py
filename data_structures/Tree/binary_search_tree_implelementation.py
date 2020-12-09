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
my_bst=BinarySearchTree()

my_bst.insert(5)
my_bst.insert(6)
my_bst.insert(4)

print(my_bst.lookup(8))
print(my_bst)
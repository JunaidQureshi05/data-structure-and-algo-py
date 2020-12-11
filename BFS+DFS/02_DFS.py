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

    def inorder(self,currentNode,my_list):
        if currentNode!=None:
            self.inorder(currentNode.left,my_list)
            my_list.append(currentNode.value)
            self.inorder(currentNode.right,my_list)
        return my_list
    
    def preorder(self,currentNode,my_list):
        if currentNode!=None:
            my_list.append(currentNode.value)
            self.preorder(currentNode.left,my_list)
            self.preorder(currentNode.right,my_list)
        return my_list
    def postorder(self,currentNode,my_list):
        if currentNode != None:
            self.postorder(currentNode.left,my_list)
            self.postorder(currentNode.right,my_list)
            my_list.append(currentNode.value)
        return my_list    
tree = BinarySearchTree()

tree.insert(100)
tree.insert(50)
tree.insert(150)
tree.insert(40)
tree.insert(80)
tree.insert(110)
tree.insert(170)

print(tree.inorder(tree.root,[]))
print(tree.preorder(tree.root,[]))
print(tree.postorder(tree.root,[]))
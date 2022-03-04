#binary tree using python

class Node:
    #constructor to create a node when object is made
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right= None
        
    #display tree
    #lets use all the methods to traverse the tree
    def preorder(self):
        print(self.data,end=" ")
        if self.left:    
            self.left.preorder()
        if self.right:    
            self.right.preorder()
            
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right:
            self.right.inorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data,end=" ")
            

#create root node
root =  Node(10)
#insert sub-tree nodes
root.left = Node(12)
root.left.left = Node(100)
root.right = Node(13)
root.right.left = Node(20)
root.right.right = Node(30)

print("preorder: ",end=" ")
root.preorder()
print("\ninorder: ",end=" ")
root.inorder()
print("\npostorder: ",end=" ")
root.postorder()

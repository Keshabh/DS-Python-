#binary tree using python

class Node:
    #constructor to create a node when object is made
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right= None
        
    def insert(self,val):
        #if value to be inserted > root data, move to right sub-tree
        if val >= self.data:
            #if self.right does not exist, then attach the node in the self.right
            if self.right is None:
                self.right = Node(val)
                return
            else:
                #use recursion and go to right sub-tree
                self.right.insert(val)
        else:
            #if left sub-tree does not exist, then attach the node to the slef.left
            if self.left is None:
                self.left = Node(val)
            else:
                #use recursion and go to left sub tree
                self.left.insert(val)
            
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

root.insert(12)
root.insert(3)
root.insert(24)
root.insert(1)

print("preorder: ",end=" ")
root.preorder()
#for verification: inorder always gives ouput in sorted order.
print("\ninorder: ",end=" ")
root.inorder()
print("\npostorder: ",end=" ")
root.postorder()
            
            
    
    

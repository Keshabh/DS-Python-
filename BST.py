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
        
        
#function to get the height of tree
#height = distance from root to farthest leaf node
def height(root):
    #lets use recursion to get the height
    #concept: get the height from left sub-tree and height from right sub-tree , keep the maximum one and
    #add 1 to it, for the root node.
    #if sub-nodes are none, it returns -1 so that height of node with 0 child nodes has -1 + 1 = 0 height.
    if root is None:
        return -1
    return max(height(root.left),height(root.right))+1

#function to do level order traversal
def level_order(root):
    #printig the nodes in tree level by level horizontally from height 0 till height h.
    #we can use BFS i.e Breadth First Search (uses Queue)
    #BFS: insert root
    # pop and insert its neighbors, and display the popped node element, continue this step,
    #till nothing is left in the queue.
    queue=[]
    queue.append(root)
    while queue:
        #dequeue the first node
        temp = queue.pop(0)
        #display the element of the node popped
        print(temp.data,end=" ")
        #insert all child nodes of element dequeue i.e temp
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

#function to do vertical order traversal
def vertical_level(root):
    pass

#function to print all the top view of a tree
def top_view(root):
    pass
            

#create root node
root =  Node(10)
#insert sub-tree nodes

root.insert(12)
root.insert(3)
root.insert(24)
root.insert(1)
root.insert(23)
root.insert(45)
root.insert(90)

print("preorder: ",end=" ")
root.preorder()
#for verification: inorder always gives ouput in sorted order.
print("\ninorder: ",end=" ")
root.inorder()
print("\npostorder: ",end=" ")
root.postorder()

print("\n\nHeight of the tree: ",height(root))
print("\nLevel Order traversal: ",end=" ")
level_order(root)
            
            
    
    

#Linked list using Python.
#Node class to create a Node.
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        
#Linked list class to store pointer of first Node in head.
class Linked_List:
    #constructor to initialize the head of linked list.
    def __init__(self):
        self.head=None
    
    #function to traverse the list and print elements inside
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.val,end=" ")
            temp=temp.next
    
    #function to insert the element in the front of the Linked_List
    def insert_front(self,data):
        #make a node using data
        new_node = Node(data)
        #if its my first node, then
        if self.head==None:
            head=new_node
        else:
            #if head is pointing to any node, it will be now second node, 
            #so whatever head is pointing, it will be pointed by new_node.
            new_node.next= self.head
            #new_node will be pointed by head, as it is first node now.
            self.head= new_node
        
    #function to insert the element at the last of the linked list
    def insert_last(self,data):
        #make a new node
        new_node = Node(data)
        #if its a first Node
        if self.head==None:
            head=new_node
        else:
            #traverse and reach the last node i.e the node whose next is None.
            temp=self.head
            while temp.next:
                temp=temp.next
            #now temp points to the last node, 
            temp.next = new_node
            
    
    #function to insert the element at the specific position of linked list
    def insert_pos(self,data):
        new_node = Node(data)
        pos = int(input("Enter the position to insert the node: "))
        #if its a first node,
        if self.head==None:
            head =  new_node
        else:
            #traverse for pos-2 times in the linked list to reach the node before pos position.
            #Ex: 1 2 3 are nodes, and user want to insert the node at thirs position and the value is 20.
            #then, it will be 1,2,20,3 ,we have to reach till 2 i.e pos-1 and head is already poiting to first node, so pos-2
            temp=self.head
            for i in range(pos-2):
                temp=temp.next
            #temp points to pos-1 positon.
            new_node.next = temp.next
            temp.next=new_node
        
    #function to delete the first node.
    def delete_front(self):
        #if linked list is empty, notify user.
        if self.head==None:
            print("linked list is empty!")
        #head should point to 2nd node.
        else:
            self.head=self.head.next
    
    #fucntion to delte last node.
    def delete_last(self):
        #if list is empty.
        if self.head==None:
            print("linked list is empty!")
        #traverse till second last node and make it next None.
        else:
            temp=self.head
            while temp.next:
                prev=temp
                temp=temp.next
            #temp points to last node, while prev points to second last node.
            prev.next = None
        
    
    #function to delete the node at specific position.
    def delete_pos(self):
        pos = int(input("Enter position to delete the node: "))
        if self.head==None:
            print("linked list is empty")
        else:
            #traverse for pos-2 times to reach till previous node of pos node.
            temp =  self.head
            for i in range(pos-2):
                temp=temp.next
            #temp points to previous node.
            temp.next =  temp.next.next
            
    
        
#Lets create 1st Node.
first_node = Node(1)
second_node= Node(2)
third_node = Node(3)

#the node create above are present in random memory locations, 
#lets link each other.

#lets first store the first node in Linked_List head pointer.

head = Linked_List()
head.head=first_node

#lets link rest of the nodes.
first_node.next = second_node
second_node.next= third_node

#lets display the elements in the linked list we created.
print("Initial Elements in Linked List are:",end=" ")
head.traverse()


#lets make a menu to perform basic insertion and deletion at different locations upon user choice
while True:
    print("\n1.Insert at front.\n2.Insert at Last\n3.Insert at specific position\n4.Delete from front.\n5.Delete at Last.\n6.Delete from specific Position.\n7.Traverse\n8.Exit Program.")
    choice=input("\nEnter your choice: ")
    
    if choice=='1':
        data=int(input("Enter data: "))
        head.insert_front(data)
    elif choice=='2':
        data=int(input("Enter data: "))
        head.insert_last(data)
    elif choice=='3':
        data=int(input("Enter data: "))
        head.insert_pos(data)
    elif choice=='4':
        head.delete_front()
    elif choice=='5':
        head.delete_last()
    elif choice=='6':
        head.delete_pos()
    elif choice=='7':
        head.traverse()
    elif choice=='8':
        break
    else:
        print("\nInvalid choice.")


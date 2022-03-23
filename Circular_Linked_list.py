#circular Linked list using Python.
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
  
    def traverse(self):
        temp=self.head
        if temp==None:
            print("list is empty!")
        else:
            while temp.next!=self.head:
                print(temp.val,end=" ")
                temp=temp.next
            print(temp.val)
                
  
    def insert_front(self,data):
        temp=self.head
        new_node=Node(data)
        if temp==None:
            self.head=new_node
            new_node.next=self.head
        else:
            new_node.next=self.head
            #we need to traverse till the end, to replace the next of the last node with new_node address.
            #last node next contains previous first node address
            #it needs to be replaced with the address of new_node.
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            self.head=new_node
                
        
   
    def insert_last(self,data):
        temp=self.head
        new_node=Node(data)
        if temp==None:
            new_node.next=self.head
            self.head=new_node
        else:
            #traverse till Last
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            
            
        
    def delete_front(self):
        temp=self.head
        if temp==None:
            print("list is empty")
        else:
            #if one element is left
            if temp.next==self.head:
                self.head=None
            else:
                #self.head=temp.next
                #traverse till the last node and change the next of last node with second node
                while temp.next!=self.head:
                    temp=temp.next
                temp.next=self.head.next
                self.head=self.head.next
                

    def delete_last(self):
        temp=self.head
        if temp==None:
            print("list is empty")
        else:
            #if one element is left
            if temp.next==self.head:
                self.head=None
            else:
                while temp.next!=self.head:
                    cur=temp
                    temp=temp.next
                cur.next=self.head
                
            
    
#lets first store the first node in Linked_List head pointer.

head = Linked_List()

#lets make a menu to perform basic insertion and deletion at different locations upon user choice
while True:
    print("\n1.Insert at front.\n2.Insert at Last\n3.Delete from front.\n4.Delete at Last.\n5.Traverse\n6.Exit Program.")
    choice=input("\nEnter your choice: ")
    
    if choice=='1':
        data=int(input("Enter data: "))
        head.insert_front(data)
    elif choice=='2':
        data=int(input("Enter data: "))
        head.insert_last(data)
    elif choice=='3':
        head.delete_front()
    elif choice=='4':
        head.delete_last()
    elif choice=='5':
        head.traverse()
    elif choice=='6':
        break
    else:
        print("\nInvalid choice.")

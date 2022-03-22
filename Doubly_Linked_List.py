#Double linked list
class Node:
    def __init__(self,val):
        self.data=val
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def traverse(self):
        temp=self.head
        if temp==None:
            print("List is empty")
            return
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    
    def insert_beg(self):
        temp=self.head
        if temp==None:
            #make first Node and assign it in head.
            val=int(input("Enter value: "))
            new_node = Node(val)
            self.head=new_node
        else:
            #if list is not empty
            val=int(input("Enter value: "))
            new_node = Node(val)
            #put new_node in prev of earlier first node
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            
    
    def insert_last(self):
        temp=self.head
        if temp==None:
            #make first Node and assign it in head.
            val=int(input("Enter value: "))
            new_node = Node(val)
            self.head=new_node
        else:
            #if list is not empty.
            #traverse till the last node.
            val=int(input("Enter value: "))
            new_node = Node(val)
            
            while temp.next!=None:
                temp=temp.next
            #now temp points to the last node.
            temp.next=new_node
            new_node.prev=temp
            
    
    def insert_random(self):
        temp=self.head
        if temp==None:
            #make first Node and assign it in head.
            val=int(input("Enter value: "))
            new_node = Node(val)
            self.head=new_node
        else:
            #if list is not empty.
            #traverse till the last node.
            val=int(input("Enter value: "))
            new_node = Node(val)
            pos=int(input("Enter position to enter the value: "))
            #travese till the pos-2, to reach the pos-1 position.
            for i in range(pos-2):
                temp=temp.next
            #temp points to pos-1 position.
            new_node.prev=temp
            new_node.next=temp.next
            temp.next.prev=new_node
            temp.next=new_node
        
    
    def delete_beg(self):
        temp=self.head
        if temp==None:
            print("list is empty")
        else:
            temp.next.prev=None
            self.head=temp.next
    
    def delete_last(self):
        temp=self.head
        if temp==None:
            print("list is empty")
        else:
            #traverse till the last
            while temp.next:
                cur=temp
                temp=temp.next
            cur.next=None
        
    def delete_random(self):
        temp=self.head
        if temp==None:
            print("list is empty")
        else:
            pos=int(input("Enter the position to delete the node: "))
            for i in range(pos-2):
                temp=temp.next
            temp.next.prev=temp
            temp.next=temp.next.next
            
        
    
#create a head of doubly linked list
head=DoublyLinkedList()

while True:
    choice=input("Press\n1.To Traverse\n2.To Insert at beg\n3.To Insert at last\n4.To Insert at random\n5.To Delete at beg\n6.To Delete at last\n7.To Delete at random\n8.To Exit\nEnter: ")
    if choice=='1': head.traverse()
    elif choice=='2':head.insert_beg()
    elif choice=='3':head.insert_last()
    elif choice=='4':head.insert_random()
    elif choice=='5':head.delete_beg()
    elif choice=='6':head.delete_last()
    elif choice=='7':head.delete_random()
    elif choice=='8':break
    else: print("Invalid choice")
    

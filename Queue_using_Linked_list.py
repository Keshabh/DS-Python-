#Queue using linked list.

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        
class Linked_List:
    def __init__(self):
        self.head=None
        
    def enqueue(self,val):
        temp=self.head
        new_node=Node(val)
        if temp==None:
            self.head=new_node
        else:
            #enqueue from the rear i.e tail of Linked_List
            #traverse till the end of list.
            while temp.next:
                temp=temp.next
            temp.next=new_node
        print(val," is pushed in the Queue")
            
    def dequeue(self):
        #if stack is empty
        temp=self.head
        if temp==None:
            print("\nQueue underflow!\n")
        else:
            k=temp.data
            self.head=temp.next
            print(k," is deleted from the Queue.")
    
    def show(self):
        #if stack is empty
        temp=self.head
        if temp==None:
            print("\nStack underflow!\n")
        else:
            print("Elements in Queue are: ")
            while temp:
                print(temp.data)
                temp=temp.next
    
#lets create an object of Linked list

root = Linked_List()

while True:
    choice = int(input("Press 1.To enqueue 2.To dequeue 3.To Show 4.To Exit.\nEnter: "))
    if choice==1:
        root.enqueue(input("Enter value to be pushed: "))
    elif choice==2:
        root.dequeue()
    elif choice==3:
        root.show()
    elif choice==4:
        break
    else:
        print("\nInvalid Choice\n")

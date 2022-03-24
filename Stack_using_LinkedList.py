#implementaton of stack using linked list.

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        
class Linked_List:
    def __init__(self):
        self.head=None
        
    def push(self,val):
        temp=self.head
        new_node=Node(val)
        if temp==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        print(val," is pushed in the stack")
            
    def pop(self):
        #if stack is empty
        temp=self.head
        if temp==None:
            print("\nStack underflow!\n")
        else:
            k=temp.data
            self.head=temp.next
            print(k," is deleted from the stack.")
    
    def show(self):
        #if stack is empty
        temp=self.head
        if temp==None:
            print("\nStack underflow!\n")
        else:
            print("Elements in stack are: ")
            while temp:
                print(temp.data)
                temp=temp.next
    
#lets create an object of Linked list

root = Linked_List()

while True:
    choice = int(input("Press 1.To Push 2.To Pop 3.To Show 4.To Exit.\nEnter: "))
    if choice==1:
        root.push(input("Enter value to be pushed: "))
    elif choice==2:
        root.pop()
    elif choice==3:
        root.show()
    elif choice==4:
        break
    else:
        print("\nInvalid Choice\n")

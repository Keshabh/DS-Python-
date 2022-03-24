#implementaton of stack using array.
#lets define the pre-defined size limit of a stack.
SIZE = 7
stack=[]

def push():
    #check if stack is overflow or not.
    if len(stack)==SIZE:
        print("\nStack is overflowed!\n")
    else:
        val=int(input("Enter the value to be pushed: "))
        stack.append(val)
        print("\nValue ",val," is pushed in the stack.\n")

def pop():
    #check for underflow condition
    if not stack:
        print("\nStack is underflowed!\n")
    else:
        k=stack.pop()
        print(k," is deleted from the stack\n")

def show():
    #check if stack is empty
    if not stack:
        print("\nStack is underflowed\n")
    else:
        print("Elements in stack are: ")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])

while True:
    choice = int(input("Press 1.To Push 2.To Pop 3.To Show 4.To Exit.\nEnter: "))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        show()
    elif choice==4:
        break
    else:
        print("\nInvalid Choice\n")

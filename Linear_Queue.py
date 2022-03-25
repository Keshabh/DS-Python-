#linear queue
#follows FIFO principle, first in first out
#The element which entered first in the queue will come out first from the queue.
queue=[]

def enqueue():
    #insert the element in the queue from the rear end.
    val = int(input("Enter value to be inserted: "))
    queue.append(val)
    print(val," is enqueued in the queue")

def dequeue():
    #dequeue the element from the front of the queue
    if not queue:
        print("Queue Underflow!")
    else:
        val = queue.pop(0)
        print(val," is dequeued from the queue")

def show():
    #display all the elements from the front till end.
    if not queue:
        print("Queue is empty!")
    else:
        print("Elements in queue are: ")
        for i in queue:
            print(i,end=" ")

while True:
    choice= input("Press 1.To Enqueue 2.To Dequeue 3.To Show 4.To Exit.\nEnter: ")
    if choice=="1":
        enqueue()
    elif choice=="2":
        dequeue()
    elif choice=="3":
        show()
    elif choice=="4":
        break
    else:
        print("\nInvalid choice\n")

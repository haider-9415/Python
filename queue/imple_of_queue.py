"""
   for creating a queue structure in the program. the following functions need to be defined
   1)enqueue() 2)isEmpty() 3)dequeue() 4)peek()

   in python, we do not need to define its size, because, it is nothing but a list
              front = 0  &  rear = len(queue) - 1
"""

def enqueue(myqueue, element):
    myqueue.append(element)
    if len(myqueue) == 1: front = rear = 0
    else: rear = len(myqueue) - 1; front = 0

def isEmpty(myqueue):
    if myqueue == []: return True
    else: return False

def dequeue(myqueue):
    if len(myqueue) == 0: front = rear = None
    else: front = 0; rear = len(myqueue) - 1
    if not(isEmpty(myqueue)): return myqueue.pop(0) 
    else: return "empty"
    # #or
    # if isEmpty(myqueue): return "empty"
    # else: return myqueue.pop(0)

def peek(myqueue):
    if isEmpty(myqueue): return "empty"
    else: return myqueue[0]

def display(myqueue):
    print("\n..................................................\n")
    if isEmpty(myqueue): print("Queue is empty"); print("\n..................................................\n")
    elif len(myqueue) == 1: print(myqueue[0],"  <-- both front & rear"); print("\n..................................................\n")
    else:
        front = 0
        rear = len(myqueue) - 1
        print(myqueue[front],"  <-- front")
        for i in range(front+1,rear):
            print(myqueue[i])
        print(myqueue[rear],"  <-- rear")
        print("\n..................................................\n")


myqueue = []

front = rear = None

while True:
    print("\noperations on queue:")
    print("1.enqueue")
    print("2.dequeue")
    print("3.peek")
    print("4.display")
    print("0.exit")

    input_val = int(input("enter the value for operation: "))

    if input_val == 1:
        value_to_insert = input("\nenter the value to insert: ")
        enqueue(myqueue,value_to_insert)

    elif input_val == 2:
        value_to_remove = dequeue(myqueue)
        if value_to_remove == "empty":
            print("\n................................................\n")
            print("queue is empty\n")
            print("\n................................................\n")
        else:
            print("\n................................................\n")
            print("removed element: ",value_to_remove)
            print("\n................................................\n")

    elif input_val == 3:
        peeked_ele = peek(myqueue)
        if peeked_ele == "empty":
            print("\n................................................\n")
            print("queue is empty\n")
            print("\n................................................\n")
        else:
            print("\n................................................\n")
            print("element at front: ",peeked_ele)
            print("\n................................................\n")

    elif input_val == 4:
        display(myqueue)

    elif input_val == 0:
        break

    else:
        print("\n................................................\n")
        print("invalid input\n")
        print("\n................................................\n")
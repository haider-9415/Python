"""
   now we will practically implement the stack with all the functions that we have learned

   then we will create an infinite loop and will ask user for the the following inputs
   1)push 2)pop 3)peek 4)display 5)exit

   then we will proceed to the respective function according to the user's input
"""

# creation of isEmpty()
def isEmpty(stack):
    if stack == []:
    # # or
    # if len(stack) == 0:
        return True
    else:
        return False

# creation of push()
def push(stack, element):
    stack.append(element)
    top = len(stack) - 1 # after adding an element 'x', top will point the 'x', therefore, it is 

# creation of pop()
def pop(stack):
    if isEmpty(stack): # if the stack is empty then which element we will pop out
        return "Underflow"
    else:
        poped_ele = stack.pop()
        if isEmpty(stack): # after deletion an element at index 'x', top will point the element at index 'x-1', therefore, it is 
            pop = None
        else:   
            pop = len(stack) - 1
        return poped_ele
    
# creation of peek()
def peek(stack):
    if isEmpty(stack):
        return "Underflow"
    else:
        top = len(stack) - 1
        return stack[top]

# creation of display()
def display(stack):
    if isEmpty(stack):
        print("\n..................................................\n")
        print("stack is empty")
        print("\n..................................................\n")
    else:
        top = len(stack) - 1 # to obtain current length of the stack
        print("\n..................................................\n")
        print("elements in stack:")
        for i in range(top,-1,-1):
            print(stack[i]) 
        print("\n................................................\n")
        


# creation of stack
stack = []

# creation of top
top = None # it will work like a pointer that points the index of stack, so, for now, top = None



while True:
    print("operations on stack\n")
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.display")
    print("0.exit")

    input_val = int(input("enter the value of operation: "))

    if input_val == 1:
        pushed_value = input("enter the value to insert: ")
        push(stack,pushed_value)

    elif input_val == 2:
        poped_ele = pop(stack)
        if poped_ele == "Underflow":
            print("\n................................................\n")
            print("stack is empty\n")
            print("\n................................................\n")
        else:
            print("\n................................................\n")
            print("poped element: ",poped_ele)
            print("\n................................................\n")

    elif input_val == 3:
        peeked_ele = peek(stack)
        if peeked_ele == "Underflow":
            print("\n................................................\n")
            print("stack is empty\n")
            print("\n................................................\n")
        else:
            print("\n................................................\n")
            print("top most element: ",peeked_ele)
            print("\n................................................\n")

    elif input_val == 4:
        display(stack)

    elif input_val == 0:
        break

    else:
        print("\n................................................\n")
        print("invalid input\n")
        print("\n................................................\n")
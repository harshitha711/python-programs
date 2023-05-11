def stack_empty():
    stack=[]
    return stack
def ISEMPTY(stack):
    return len(stack)==0
def push(stack,n):
    stack.append(n)
def pop(stack):
    if(ISEMPTY(stack)):
        print("stack is full")
    else:
        return stack.pop()
def show(stack):
    for i in stack:
        print(i)
stack=stack_empty()
pop(stack)
show(stack)


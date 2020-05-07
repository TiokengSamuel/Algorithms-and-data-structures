from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print("Stack size: ", stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')

print("Full size: ", stack.full())
print("Stack is :", stack)

print("\n Popping every element in stack")
print(stack.get())
print(stack.get())
print(stack.get())

print("Is stack empty: ", stack.empty())

import random

class Stack:
    def __init__(self):
        self.container = []

    def isEmpty(self):
        return self.container == []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[len(self.container) - 1]

    def size(self):
        return len(self.container)

    def pushMethod(self, n, m):
        for i in range(0, n, m):
            self.push(random.randint(1,10))
        print(self.size())
        # return stack1

    def popMethod(self, n, m):
        for i in range(0, n, m):
            self.pop()
        print(self.size())

    def peekMethod(self):
            print(self.peek())

    def checkIfEmpty(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack is not empty - Size: " + str(self.size()))
'''
    Because push and pop both work with the same end of the stack, the front, the complexity will be constant, O(n).
    This also means that isempty and size will also be constant time complexities.
'''

'''
experimented with different parameter sizes
'''
stack1 = Stack()

stack1.pushMethod(10000000,10)
stack1.popMethod(1000000, 10)
stack1.peekMethod()
stack1.checkIfEmpty()

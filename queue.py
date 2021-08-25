import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueueMethod(self, n, m):
        for i in range(0, n, m):
            self.enqueue(random.randint(1, 10))
        print(self.size())
        # return stack1

    def dequeueMethod(self, n, m):
        for i in range(0, n, m):
            self.dequeue()
        print(self.size())

    ### this method checks for both the size and if it is empty
    def checkIfEmpty(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Queue is not empty - Size: " + str(self.size()))

''' 
    All of these methods besides enqueue will have a constant runtime complexity. The enqueue method adds 
    an item to the rear of the data and since it runs under the rule of First In First Out, the queue method will 
    result in a linear complexity. The rest of the methods will be constant. The dequeue makes sense to be linear 
    because it removes the front item from the list. And the size and isempty methods result in the same complexity.
'''

'''
experimented with different parameter sizes
'''
queue1 = Queue()
queue1.enqueueMethod(100000, 10)
queue1.dequeueMethod(1000, 10)
queue1.checkIfEmpty()
queue1.size()

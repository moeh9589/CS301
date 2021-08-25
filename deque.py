import random

class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFrontMethod(self, n, m):
        for i in range(0, n, m):
            self.addFront(random.randint(1, 10))
        print(self.size())

    def addRearMethod(self, n, m):
        for i in range(0, n, m):
            self.addRear(random.randint(1, 10))
        print(self.size())

    def removeFrontMethod(self, n, m):
        for i in range(0, n, m):
            self.removeFront()
        print(self.size())

    def removeRearMethod(self, n, m):
        for i in range(0, n, m):
            self.removeRear()
        print(self.size())

    ### this method checks for both the size and if it is empty
    def checkIfEmpty(self):
        if self.isEmpty():
            print("Deque is empty.")
        else:
            print("Deque is not empty - Size: " + str(self.size()))

'''
    All of these methods should be running with a constant time complexity, O(1), due to the fact that it is 
    double ended. This structure allows for each node at the beginning and end to be quickly accessed whether 
    removing or adding to the front/rear. With this comes a little more complexity of modifying the data at the
    middle. If a middle-modifying method were to be implemented, then a linear complexity would be introduced.
'''

'''
experimented with different parameter sizes
'''
deque1 = Deque()
deque1.addFrontMethod(50000, 10)
deque1.addRearMethod(50000, 10)
deque1.removeFrontMethod(50000, 10)
deque1.removeRearMethod(50000, 100)
deque1.checkIfEmpty()
import random

class Node:
    def __init__(self,initdata, position = 0):
        self.data = initdata
        self.next = None
        self.position = position

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def appendMethod(self, item):
        #for i in range (10000,10):
            current = self.head
            if current:
                while current.getNext() != None:
                    current = current.getNext()
                current.setNext(Node(item))
            else:
                self.head = Node(item)


    def indexMethod(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                print("item found")
                return current.position

            else:
                current = current.next
                #print("item not present at this index")

    def insertMethod(self, item, position):
        temp = Node(item)
        current = self.head
        previous = None
        count = 0
        found = False
        if position > self.size() - 1:
            print("Position must be within size of list.")

        while current is not None and not found:
            if count == position:
                found = True
            else:
                previous = current
                current = current.getNext()
                count += 1

        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def popMethod(self, pos):
        current = self.head
        previous = None
        found = False
        if current:
            count = 0
            while current.getNext() is not None and not found:
                if count == pos:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
                    count += 1
            if previous is None:
                self.head = current.getNext()
                if current.getNext() is None:
                    self.tail = current.getNext()
            else:
                self.tail = previous
                previous.setNext(current.getNext())

        return current.getData()

    def PrintList( self ):
        node = self.head

        while node != None:
            print (node.data)
            node = node.next

linkedlist = UnorderedList()

for i in range(10000):
    x = random.randint(1, 100)
    linkedlist.add(1)

print(linkedlist.size())
print(linkedlist.search(93))
print(linkedlist.search(1))

for i in range(101):
    linkedlist.remove(1)
print(linkedlist.size())

linkedlist.appendMethod(1001)
'''
this method looks at every node and prints out the result of whether the index is true or false based on the input
'''
linkedlist.indexMethod(1001)
'''
this will find 1 at the first index so no further looking is needed. 
The previous line won't find 1001 until the last node
'''
linkedlist.indexMethod(1)

linkedlist.insertMethod(1200000,12)
print(linkedlist.search(1200000))

for i in range(101):
    linkedlist.popMethod(100)

print(linkedlist.size())

##linkedlist.PrintList()

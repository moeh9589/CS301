'''
logic inspred from https://stackabuse.com/doubly-linked-list-with-python-examples/
'''

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.previous = None


class OrderedList():
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def insertAtEnd(self, data):
        if self.head is None:
            new_node = QNode(data)
            self.head = new_node
            return
        n = self.head

        while n.next is not None:
            n = n.next
            new_node = Node(data)
            n.next = new_node
            new_node.previous = n

    def deleteAtStart(self):
        if self.head is None:
            print("Cannot perform function")
            return

        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head = None

    def deleteAtEnd(self):
        if self.head is None:
            print("Cannot perform function")
            return

        if self.head.next is None:
            self.head = None
            return
        n = self.head

        while n.next is not None:
            n = n.next
        n.previous.next = None

    def search(self, value):
        i = 1;
        inList = False;
        current = self.head;

        if (self.head == None):
            print("List is empty");
            return;

        while (current != None):

            if (current.item == value):
                inList = True;
                break;
            current = current.next;
            i = i + 1;

        if (inList):
            print("Node is present in the list at the position : " + str(i));
        else:
            print("Node is not present in the list");

    def enqueue(self, data):
        if self.head is None:
            new_node = QNode(data)
            self.head = new_node
            return
        n = self.head

        while n.next is not None:
            n = n.next
            new_node = QNode(data)
            n.next = new_node
            new_node.previous = n



DLL = OrderedList()

DLL.insertAtStart(10)
DLL.insertAtEnd(101)
#DLL.deleteAtStart()

DLL.insertAtEnd(2)
DLL.insertAtEnd(2)
DLL.insertAtEnd(2)
DLL.insertAtEnd(2)
#DLL.deleteAtEnd()

DLL.search(2)
DLL.search(101)
DLL.search(10)

'''
ANSWERS to 6 & 7:
'''
'''
#6    Python's representation of a list seems to be most close to a linked list. The reasoning behind this is 
      because with a doubly linked list, data can be added to either end of the list with a constant time complexity.
      With a python list the previous element must be known when referencing any element. This is the same in a 
      linked list.
    
#7    Doubly linked lists are going to have O(1) for inserting and deleting elements from the list. Linked lists are going
      to have O(n) for the same methods. This leads me to assume that doubly linked lists are going to have the best 
      running times when implemented with other data structures. Doubly linked lists can be accessed in both directions, 
      providing a quicker run time with the only caveat being that it will take up more memory space.
'''
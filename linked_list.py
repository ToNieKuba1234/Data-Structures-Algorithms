#This is a singly linked list that imitate's basic
#functions of python's native list data structure  (Without the implementation of tail!)
#Complete list of features:
# - Constructor
# - append()
# - insert()
# - pop()
# - remove()
# - extend()
# - length()
# - __str__()
class MyList:
    class Node:  #this is a singular node cell, containing data, and other cell class
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, *data_arr):  #This is the constructor, initializes head and add's all the data added with constructor
        self.head = None

        for data in data_arr:
            self.append(data)
    
    def append(self, data):  #this function can add one value to MyList
        node = self.Node(data)
        if self.head is None:
            self.head = node
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            currNode.next = node
    
    def extend(self, *data_arr):  #this function can add multiple values to MyList
        for data in data_arr:
            self.append(data)
    
    def insert(self, index, data):  #this function will add an element at a specific index in the array
        if index < 0 or index > self.length():
            raise IndexError("Index out of range!")
        
        newNode = self.Node(data)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            currNode = self.head

            for _ in range(index - 1):
                currNode = currNode.next
            
            newNode.next = currNode.next
            currNode.next = newNode

    
    def pop(self, index=-1):  #will remove an element by its index
        if self.length() == 0:
            raise IndexError("Index out of range!")
        
        if index == -1:
            index = self.length() - 1

        if index < 0 or index > self.length():
                raise Exception("Index out of range")

        if index == 0:
            removed = self.head
            self.head = self.head.next

            return removed.data
            
            
        prevNode = self.head
        currNode = self.head.next
        idx = 1

        while idx < index:
            prevNode = currNode
            currNode = currNode.next

            idx += 1
            
        prevNode.next = currNode.next
        return currNode.data

    def remove(self, data): #will remove element by its value, not by its index like in pop()
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        prevNode = self.head
        currNode = self.head.next

        while currNode.next:
            if currNode.data == data:
                break

            prevNode = currNode
            currNode = currNode.next
        
        prevNode.next = currNode.next
    
    def length(self):  #will return the total amount of elements in the linked list
        length = 0
        currNode = self.head
        while currNode:
            length += 1
            currNode = currNode.next
        
        return length
    
    def __str__(self):  #what will be show when we print the whole class
        result = ""
        result += str(self.head.data)

        currNode = self.head.next
        while currNode:
            result += f", {currNode.data}"
            currNode = currNode.next
        
        return result

#makes this run only if the script is runned by python linked_list.py
if __name__ == "__main__":
    #Constructor
    myList = MyList(1, 2, 3)
    
    #append func
    myList.append(4)

    #pop func
    myList.pop(1)

    #remove func
    myList.remove(4)

    #insert func
    myList.insert(2, 5)

    #extend func
    myList.extend(5, 6, 7)

    #length func
    print(f"Length of my MyList is: {myList.length()}")

    #display func
    print(myList)
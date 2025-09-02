#This is a simple python Heap implementation
# that includes these features:
# - constructor()
# - push()
# - pop()
# - display()

import math

class myHeap():
    def __init__(self, iterable):
        self.data = []

        for i in iterable:
            self.data.append(i)
            
    def push(self, value):  #adds an element to the heap
        self.data.append(value)
        self.bubble_up(len(self.data) - 1)
        
    
    def pop(self):  #removes the smallest element (biggest in max-heap)
        if not self.data:
            raise Exception("Cannot remove an element from an empty list!")

        removed_val = self.data[0]

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.data.pop(-1)

        self.bubble_down(0)


    def bubble_up(self, index):  #keeps the tree heapified (the parent has to be smaller than the children)
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index] < self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    
    def bubble_down(self, index):  #keeps the tree heapified (the parent has to be smaller than the children)
        length = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < length and self.data[left] < self.data[smallest]:
                smallest = left

            if right < length and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == index:
                break

            
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    
    def display(self):  #prints out the tree to the screen
        if not self.data:
            print("(pusty kopiec)")
            return

        levels = math.floor(math.log2(len(self.data))) + 1  #func calculating height of the heap
        max_width = 2 ** (levels - 1)

        index = 0
        for level in range(levels):
            count = min(2 ** level, len(self.data) - index)

            spaces = max_width // (2 ** level)
            line = " " * (spaces // 2)

            for i in range(count):
                line += f"{self.data[index]:^3}" + " " * spaces
                index += 1

            print(line.rstrip()) 
        print()


#makes this run only if the script is runned by python heap.py
if __name__ == "__main__":
    #initializing the heap
    myHeap = myHeap([1, 2])

    #adding elements to the heap
    myHeap.push(5)
    myHeap.push(3)
    myHeap.push(8)

    #removing an element from the heap
    myHeap.pop()

    #siplaying the heap
    myHeap.display()


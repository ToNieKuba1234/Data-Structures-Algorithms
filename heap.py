#This is a simple python Heap implementation
# that includes these main features:
# - constructor()
# - push()
# - pop()
# - heapify()
# - peek()
# - display()
# - utility functions(is_empty(), size(), bubble_up(), bubble_down())

import math

class myHeap():
    def __init__(self, iterable):
        self.data = list(iterable)
        self.heapify()
            
    def push(self, value):  #adds an element to the heap
        self.data.append(value)
        self.bubble_up(len(self.data) - 1)
        
    
    def pop(self):  #remove's the smallest element and returns it
        if self.is_empty():
            raise Exception("Cannot remove an element from an empty heap!")

        removed_val = self.data[0]

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.data.pop(-1)

        if not self.is_empty():  # tylko jeśli po usunięciu nadal są elementy
            self.bubble_down(0)

        return removed_val

    def heapify(self):  #changes a list so it's a heap (min-heap)
        if self.is_empty():
            return
        
        last_parent = (self.size() - 2) // 2

        for index in range(last_parent, -1, -1):
            self.bubble_down(index)


    def peek(self):  #returns the smallest element
        if self.is_empty():
            raise Exception("Cannot peek into an empty heap!")
        return self.data[0]

    
    def size(self):  #returns the heap size
        return len(self.data)
    
    def is_empty(self):
        return self.size() == 0


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
        if self.is_empty():
            print("(pusty kopiec)")
            return

        levels = math.floor(math.log2(self.size())) + 1  # korzystamy z size()
        max_width = 2 ** (levels - 1)

        index = 0
        for level in range(levels):
            count = min(2 ** level, self.size() - index)

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

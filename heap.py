#This is a simple python Heap implementation
# that includes these features:
# - push()
# - display()

class myHeap():
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)
        self.bubble_up(len(self.data) - 1)

    def bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index] < self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break
    
    def display(self):
        level = 0
        next_level = 1

        for i, value in enumerate(self.data):
            print(value, end=" ")
            if i == next_level - 1:
                print()
                level += 1
                next_level += 2 ** level
        
        print()

#makes this run only if the script is runned by python heap.py
if __name__ == "__main__":
    myHeap = myHeap()


    myHeap.push(5)
    myHeap.push(3)
    myHeap.push(8)
    myHeap.push(1)
    myHeap.push(2)

    myHeap.display()
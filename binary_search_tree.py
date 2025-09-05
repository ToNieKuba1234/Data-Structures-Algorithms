#This is my implementation of binary
#search tree in python, including
#these features: (will add more)
# - constructor
# - append()
# - pop()

class MyTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self, iterable):
        self.root = None

        for data in iterable:
            self.append(data)
    
    def append(self, data):
        if self.root is None:
            self.root = self.Node(data)
        
        prevNode = None
        currNode = self.root
        while currNode:
            if currNode.data < data:
                prevNode = currNode
                currNode = currNode.right
            
            else:
                prevNode = currNode
                currNode = currNode.left
        
        if data < prevNode.data:
            prevNode.left = self.Node(data)
        else:
            prevNode.right = self.Node(data)
    
    def pop_max(self):
        ...


    def pop_min(self):
        ...

#makes this run only if the script is runned by python binary_search_tree.py
if __name__ == "__main__":
    myTree = MyTree([2, 16, 1])

    myTree.append(8)

    myTree.display()

class BTNode:
    def __init__(self, value):
        self.value = value 
        self.left=None
        self.right=None
        # self.next= None 

# Create an add(val) method on the BST object to add new value to the tree. This entails creating a BTNode with this value and connecting it at the appropriate place in the tree. Unless specified otherwise, BSTs can contain duplicate values.

    def add(self, value):
        if self.value == value:
            return False
        elif self.value > value:
            if self.left:
                return self.left.add(value)
            else:
                self.left = BTNode(value)
                return True
        else:
            if self.right:
                return self.right.add(value)
            else:
                self.right = BTNode(value)
                return True

# Create a contains(val) method on BST that returns whether the tree contains a given value. Take advantage of the BST structure to make this a much more rapid operation than SList.contains() would be.

    def contains(self, value):
        if (self.value == value):
            return True
        elif self.value > value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(value)
            else:
                return False

# Create a min() method on the BST class that returns the smallest value found in the BST.

    def min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value


# Create a max() BST method that returns the largest value contained in the binary search tree.


    def max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value


class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root:
            return self.root.add(value)
        else:
            self.root = BTNode(value)
            return True

    def contains(self, value):
        if self.root:
            return self.root.contains(value)
        else:
            return False

    def min(self, value):
        if self.root:
            return self.root.min()
        else:
            return False

    def max(self, value):
        if self.root:
            return self.root.max()
        else:
            return False

bst = BST()
bst.add(5)
bst.add(8)
bst.add(34)
bst.add(12)
bst.add(9)
bst.add(25)
bst.add(60)
bst.add(1)

print(bst.contains(8))
print(bst.contains(10))
print(bst.min(bst.root))
print(bst.max(bst.root))


    

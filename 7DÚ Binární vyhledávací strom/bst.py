class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.visited = 0

    def insert(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
        else:
            curr = self.head
            end = False
            while not end:
                if value < curr.value:
                    if curr.left is None:
                        curr.left = new
                        end = True
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = new
                        end = True
                    else:
                        curr = curr.right

    def fromArray(self, array):
        for items in array:
            self.insert(items)

    def search(self, value):
        self.visited = 0
        found = False
        curr = self.head
        while curr is not None:
            if curr.value == value:
                self.visited += 1
                return True
            else:
                if value < curr.value:
                    curr = curr.left
                else:
                    curr = curr.right
                self.visited += 1
        return False

    def min(self):
        self.visited = 1
        curr = self.head
        if curr is not None:
            while curr.left is not None:
                curr = curr.left
                self.visited += 1
            return curr.value
        else:
            return None

    def max(self):
        self.visited = 1
        curr = self.head
        if curr is not None:
            while curr.right is not None:
                curr = curr.right
                self.visited += 1
            return curr.value
        else:
            return None

    def visitedNodes(self):
        return self.visited


# bst2 = BinarySearchTree()
# bst2.fromArray([5, 3, 1, 4, 7, 6, 8])

# print(bst2.search(5))
# print(bst2.visitedNodes())
# print(bst2.search(7))
# print(bst2.visitedNodes())
# print(bst2.search(6))
# print(bst2.visitedNodes())
# print(bst2.search(10))
# print(bst2.visitedNodes())
# print("MIN: " + str(bst2.min()))
# print(bst2.visitedNodes())
# print("MAX: " + str(bst2.max()))
# print(bst2.visitedNodes())

"""
Author: Ibad Rather
email: ibad.rather.ir@gmail.com
Date: 02-04-2021
"""

"""
Binary Tree can can have at max two elements at each node.

Binary Search Tree: It is a binary tree with a specific order where Left Search Tree has all the elements
which are less than the current node and Right Search Tree has all greater node elements.

One of the utilities of Binary Search tree is that it puts the elements of a list in a particular order.

It also removes duplicates from the given list.

To implement a set, this can be very useful.

It has O(logn) Complexity
"""


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # add child method
    def add_child(self, data):
        if data == self.data:       # if data already exists we just return, because it cant have duplicate data
            return

        if data < self.data:        # add data to left subtree
            if self.left:           # see if the node has data
                self.left.add_child(data)       # recursive call add_child() method
            else:
                self.left = BinarySearchTreeNode(data)
        else:                       # add data to right subtree
            if self.right:          # see if the node has data
                self.right.add_child(data)      # recursive call add_child() method
            else:
                self.right = BinarySearchTreeNode(data)

    # In order Traversal Method Implementation
    # We can use this method to print all elements in the Binary Tree
    def in_order_traversal(self):
        """
        In order traversal means we are first visiting left subtree, then base node and finally the right trees
        :return: list of binary tree elements
        """
        elements = []       # list to store elements of binary tree
        # Visit Left Tree First
        if self.left:       # check if there are elements on the left side of tree
            elements += self.left.in_order_traversal()      # recursively calling the function

        # Now we want this recursion to end some time
        # Visit the Base Node
        elements.append(self.data)

        # Visit Right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    # Pre Order Traversal
    def pre_order_traversal(self):
        """
        Pre Order Traversal means visit base node, then left nodes and finally right nodes
        :return:
        """
        elements = []
        # Visit Node Base
        elements.append(self.data)

        # Visit left Tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit Right Tree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    # Post Order Traversal
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    # Sum of elements of the Tree
    def sum_tree(self):
        elements = self.in_order_traversal()        # get elements of the tree
        return sum(elements)                        # return the sum

    # Maximum element in the Tree
    def max_tree(self):
        # Max element will be right most
        maximum = self.data
        # We will traverse until we reach right most element
        if self.right:
            maximum = self.right.max_tree()
            return maximum
        else:
            return maximum

    def min_tree(self):
        # Min element will be left most
        minimum = self.data
        # We will traverse until we reach left most element
        if self.left:
            minimum = self.left.max_tree()
            return minimum
        else:
            return minimum

    # Search Method to search for some value
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(val)      # recursive search
            else:
                return False
        if val > self.data:
            # value might be in right sub tree
            if self.right:
                return self.right.search(val)
            else:
                return False


# Helper method to build Binary Tree
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [15, 12, 7, 14, 27, 20, 23, 88 ]   # removes duplicates automatically
    number_tree = build_tree(numbers)
    # See if a value exists in the tree
    print("Is present? ", number_tree.search(1000))
    print("Sum: ", number_tree.sum_tree())
    print("Max: ", number_tree.max_tree())
    print("Min: ", number_tree.min_tree())
    print("In - OT", number_tree.in_order_traversal())
    print("Pre- OT", number_tree.pre_order_traversal())
    print("Post - OT", number_tree.post_order_traversal())




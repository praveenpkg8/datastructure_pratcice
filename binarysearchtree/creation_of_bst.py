# Day: 4 | 03/08/2019
"""
Insertion of binary search tree
"""


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def pre_order(root):

    if root is None:
        return
    print(root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        current_node = self.root
        while True:
            if current_node.data < val:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(val)
                    break
            else:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(val)
                    break


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)

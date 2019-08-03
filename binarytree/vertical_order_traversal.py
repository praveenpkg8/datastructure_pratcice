# Day 2: 02/08/2019 vertical order traversal


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def find_max_tree(_root, minimum, maximum, hd):
    if _root is None:
        return

    if hd < minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd

    find_max_tree(_root.left, minimum, maximum, hd - 1)
    find_max_tree(_root.right, minimum, maximum, hd + 1)


def print_vertical_line(root, line_no, hd):
    if root is None:
        return
    if hd == line_no:
        print(root.data, end=' ')

    print_vertical_line(root.left, line_no, hd - 1)
    print_vertical_line(root.right, line_no, hd + 1)


def vertical_order(_root):
    minimum = [0]
    maximum = [0]
    find_max_tree(_root, minimum, maximum, 0)

    for line_no in range(minimum[0], maximum[0] + 1):
        print_vertical_line(_root, line_no, 0)
        print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

vertical_order(root)

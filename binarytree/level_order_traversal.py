# Day 2: 02/08/2019


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def max_depth(_root):
    if _root is None:
        return 0

    else:

        left_depth = max_depth(_root.left)
        right_depth = max_depth(_root.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


def get_level_order(_root):
    height = max_depth(_root)
    level_order = []

    for d in range(1, height + 1):
        get_given_level(_root, d, level_order)

    return level_order


def get_given_level(_root, level, level_order):
    if _root is None:
        return

    if level == 1:
        level_order.append(_root.data)

    elif level > 1:
        get_given_level(_root.left, level - 1, level_order)
        get_given_level(_root.right, level - 1, level_order)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

level_view = get_level_order(root)
print(level_view)

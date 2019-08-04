# Day 3: 02/08/2019 vertical order traversal using map


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def get_vertical_order(root, hd, m):
    if root is None:
        return

    try:
        m[hd].append(root.data)
    except KeyError:
        m[hd] = [root.data]

    get_vertical_order(root.left, hd - 1, m)
    get_vertical_order(root.right, hd + 1, m)


def dict_vertical_order(root):
    m = dict()
    hd = 0
    new_dict = {}
    get_vertical_order(root, hd, m)
    for index, value in enumerate(sorted(m)):
        new_dict[value] = m[value]
    return new_dict



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

vertical_order = dict_vertical_order(root)
print(vertical_order)

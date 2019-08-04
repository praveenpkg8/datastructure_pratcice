# Day 4: 03/08/2019 implementation


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def max_depth(root):
    if root is None:
        return 0

    else:

        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


def get_level_order(root):
    height = max_depth(root)
    level_order_list = []

    for i in range(1, height + 1):
        get_given_level(root, i, level_order_list)

    return level_order_list


def get_given_level(root, level, level_order_list):
    if root is None:
        return None

    if level == 1:
        level_order_list.append(root.data)

    elif level > 1:
        get_given_level(root.left, level - 1, level_order_list)
        get_given_level(root.right, level - 1, level_order_list)


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


def top_view(_level_order, _vertical_order):
    for index in _vertical_order:
        if len(_vertical_order.get(index)) == 1:
            print(_vertical_order.get(index)[0], end=' ')
        elif len(_vertical_order.get(index)) > 1:
            for i in _level_order:
                if i in _vertical_order.get(index):
                    print(i, end=' ')
                    break


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

level_order = get_level_order(root)
vertical_order = dict_vertical_order(root)
top_view(level_order, vertical_order)

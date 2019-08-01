
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






class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1


class AVL_Tree(object):

    def insert(self, root, data):

        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_height(self, root):
        if root is None:
            return 0

        return root.height

    def get_balance(self, root):
        if root is None:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotate(self, z):

        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):

        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def pre_order(self, root):

        if root is None:
            return

        print(root.data, end=' ')
        self.pre_order(root.left)
        self.pre_order(root.right)


avl_tree = AVL_Tree()

elements = [int(x) for x in input().split()]

root = None

for element in elements:
    root = avl_tree.insert(root, element)

avl_tree.pre_order(root)

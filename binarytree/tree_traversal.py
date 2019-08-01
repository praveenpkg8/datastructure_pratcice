
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def print_in_order(root):

    if root:
        print_in_order(root.left)
        print(root.data, end=' ')
        print_in_order(root.right)


def print_pre_order(root):

    if root:
        print(root.data, end=' ')
        print_pre_order(root.left)
        print_pre_order(root.right)


def print_post_order(root):

    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.data, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(" pre order: ")
print_pre_order(root)
print("\n post order: ")
print_post_order(root)
print("\n in order: ")
print_in_order(root)




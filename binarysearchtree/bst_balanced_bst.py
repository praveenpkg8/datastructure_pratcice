class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def insert_bst(node, data):
    if node.data > data:
        if node.left is None:
            node.left = Node(data)
        else:
            insert_bst(node.left, data)

    elif node.data < data:
        if node.right is None:
            node.right = Node(data)
        else:
            insert_bst(node.right, data)


def inorder_list_bst(node, inorder_list):
    if node is None:
        return node

    inorder_list_bst(node.left, inorder_list)
    inorder_list.append(node)
    inorder_list_bst(node.right, inorder_list)


def print_pre_order(node):
    if node is None:
        return node

    print(node.data, end=' ')
    print_pre_order(node.left)
    print_pre_order(node.right)


def self_balanced_bst(element_list, start, end):
    if start > end:
        return

    mid = (start + end) // 2
    node = element_list[mid]

    node.left = self_balanced_bst(element_list, start, mid - 1)
    node.right = self_balanced_bst(element_list, mid + 1, end)
    return node


elements = [int(x) for x in input().split()]

root = Node(elements.pop(0))
for element in elements:
    insert_bst(root, element)

element_list = []
inorder_list_bst(root, element_list)
len_element = len(element_list)
root = self_balanced_bst(element_list, 0, len_element - 1)
print_pre_order(root)

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def print_post_order_traversal(root):

    if root:
        print_post_order_traversal(root.left)
        print_post_order_traversal(root.right)
        print(root.data, end=' ')


def min_value_node(node):

    current = node

    while current.left is not None:
        current = current.left

    return current


def delete_node(root, data):

    if root is None:
        return

    if root.data > data:
        root.left = delete_node(root.left, data)

    elif root.data < data:
        root.right = delete_node(root.right, data)

    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)

        root.data = temp.data

        root.right = delete_node(root.right, temp.data)

    return root


def insert_to_bst(root, value):

    if root.data > value:

        if root.left is None:
            root.left = Node(value)
        else:
            insert_to_bst(root.left, value)

    elif root.data < value:

        if root.right is None:
            root.right = Node(value)
        else:
            insert_to_bst(root.right, value)


if __name__ == '__main__':
    tree_entity = list(map(int, input().split()))
    root = Node(tree_entity.pop(0))
    for entity in tree_entity:
        insert_to_bst(root, entity)
    print_post_order_traversal(root)
    root = delete_node(root, 8)
    print()
    print_post_order_traversal(root)


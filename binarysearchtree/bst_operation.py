class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def print_in_order_traversal(root):
    if root:
        print_in_order_traversal(root.left)
        print(root.data, end='')
        print_in_order_traversal(root.right)


def insert_to_bst(current_node, value):
    if current_node.data > value:
        if current_node.left is None:
            current_node.left = Node(value)

        else:
            insert_to_bst(current_node.left, value)
    elif current_node.data < value:
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            insert_to_bst(current_node.right, value)


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_to_bst(root, value):
    if root is None:
        return

    if root.data > value:
        root.left = delete_to_bst(root.left, value)

    elif root.data < value:
        root.right = delete_to_bst(root.right, value)

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
        root.right = min_value_node(root.right, temp.data)

    return root


def check_for_operation(current_node, ops):
    node = current_node
    for current_entity in ops:
        if current_entity[0] == 'i':
            insert_to_bst(node, current_entity[1])
        elif current_entity[0] == 'd':
            node = delete_to_bst(node, current_entity[1])
    return node


if __name__ == '__main__':
    number_of_operation = int(input())
    operations_list = []
    for i in range(number_of_operation):
        operations_list.append(tuple(input().split(' ')))
    operation = operations_list.pop(0)
    if operation[0] == 'i':
        root = Node(operation[1])
    root = check_for_operation(root, operations_list)
    print_in_order_traversal(root)

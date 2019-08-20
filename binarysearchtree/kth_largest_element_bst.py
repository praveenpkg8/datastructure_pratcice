class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def kth_largest_element(root, k, c):

    if root is None or c[0] >= k:
        return

    kth_largest_element(root.right, k, c)

    c[0] += 1

    if c[0] == k:
        print('{1}th largest element {0}'.format(root.data, k))
        return

    kth_largest_element(root.left, k, c)






def insert_bst(root, data):

    if root.data > data:

        if root.left is None:
            root.left = Node(data)

        else:
            insert_bst(root.left, data)

    elif root.data < data:

        if root.right is None:
            root.right = Node(data)

        else:
            insert_bst(root.right, data)


k = int(input())
elements = [int(x) for x in input().split()]
root = Node(elements.pop(0))
for element in elements:
    insert_bst(root, element)
c = [0]
kth_largest_element(root, k, c)





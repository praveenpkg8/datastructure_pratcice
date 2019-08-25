def search(value):

    if value >= 0:
        if has[value][0] == 1:
            return 'True'
        else:
            return 'False'

    elif has[abs(value)][1] == 1:
        return 'True'

    return 'False'


def insert(elements, len_elements):

    for i in range(0, len_elements):
        if elements[i] >= 0:
            has[elements[i]][0] = 1
        else:
            has[abs(elements[i])][1] = 1


elements = [-1, 9, -5, 8, -5, -2]
len_elements = len(elements)
MAX = 1000

has = [[0 for i in range(2)] for j in range(MAX + 1)]

insert(elements, len_elements)

x = -5

print(search(x))


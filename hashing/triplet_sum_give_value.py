def find_three_numbers(elements, length, _sum):
    for i in range(length - 1):
        s = set()
        current_sum = _sum - elements[i]
        for j in range(i + 1, length):
            if current_sum - elements[j] in s:
                print('triplets: ({0}, {2}, {1})'.format(elements[i], elements[j], current_sum - elements[j]))
            s.add(elements[j])
    return


elements = [1, 4, 45, 6, 10, 8, 11]
triple_sum = 22
elements_size = len(elements)
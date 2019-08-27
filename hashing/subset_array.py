

def hash_element(element):
    return element % 10


def is_subset(elements, sub_elements):
    dict_elements = {}
    for element in elements:
        if dict_elements.get(hash_element(element)) is None:
            dict_elements[hash_element(element)] = [element]
        else:
            entity = dict_elements.get(hash_element(element))
            entity.append(element)
            dict_elements[hash_element(element)] = entity

    for element in sub_elements:
        if dict_elements.get(hash_element(element)) is None:
            return False

    return True


elements = [11, 1, 13, 21, 3, 7]
sub_elements = [11, 3, 7, 1]
print(is_subset(elements, sub_elements))

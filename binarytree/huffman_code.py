import queue as Queue


class Node:

    def __init__(self, freq, data):
        self.left = None
        self.right = None
        self.data = data
        self.freq = freq


def character_hidden_code(current_object, code):

    if current_object is None:
        return
    elif current_object != '\0':
        character_code[current_object.data] = code

    character_hidden_code(current_object.right, code + '1')
    character_hidden_code(current_object.left, code + '0')


def construct_huffman_tree(freq):

    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        current_object = Node(a[0] + b[0], '\0')
        current_object.left = a[2]
        current_object.right = b[2]
        q.put((current_object.freq, current_object.data, current_object))

    root = q.get()
    root = root[2]
    return root


def generate_decode_string(string, code_hidden):

    decoded_string = ''
    for character in input_string:
        decoded_string += code_hidden[character]
    return decoded_string


def get_character_frequency(string):

    character_freq = {}
    for character in string:
        character_freq[character] = input_string.count(character)
    return character_freq


def decode_huffman(root, decoded_string):

    temp = root

    for char in decoded_string:

        if char == '0':
            temp = temp.left
        elif char == '1':
            temp = temp.right

        if temp.right is None and temp.left is None:
            print(temp.data, end='')
            temp = root


if __name__ == '__main__':

    input_string = input()
    freq = get_character_frequency(input_string)
    root = construct_huffman_tree(freq)
    character_code = {}
    character_hidden_code(root, '')
    decoded_string = generate_decode_string(input_string, character_code)
    print(decoded_string)
    decode_huffman(root, decoded_string)

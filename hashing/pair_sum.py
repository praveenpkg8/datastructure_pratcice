def is_pair_sum(elements, sum):
    for element in elements:
        hash_element[element] += 1

    left = 0
    right = 100000

    while left < right:
        if hash_element[left] == 0 or hash_element[right] == 0:
            while hash_element[left] == 0:
                left += 1
            while hash_element[right] == 0:
                right -= 1

        if left + right == sum and left != right:
            return True
        elif left + right > sum:
            right -= 1
        elif left + right < sum:
            left += 1

        if left + right == sum and left == right and hash_element[left] > 1:
            return True

    return False


hash_element = [0] * 1000001
elements = [1, 2, 3, 4, 5]
pair_sum = 7
count = 0
print(is_pair_sum(elements, pair_sum))

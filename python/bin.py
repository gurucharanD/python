import math

elements = [1, 2, 3, 4, 6, 7, 8, 100, 344, 987, 999]
key = 1500


def binary_search(elements, left, right, key):
    mid = math.floor((left+right)/2)
    print(left, right, mid)
    if elements[mid] == key:
        print('key found', key)
        return
    if mid == len(elements)-1:
        print('key not found')
        return
    if key < elements[mid]:
        right = mid-1
        return binary_search(elements, left, right, key)
    if key > elements[mid]:
        left = mid+1
        return binary_search(elements, left, right, key)


binary_search(elements, 0, len(elements)-1, key)

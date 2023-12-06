def isSubset(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return set1.issubset(set2)


def is_subset(arr1, arr2):
    hash_table = {}

    for value in arr2:
        if value not in hash_table:
            hash_table[value] = True

    for value in arr1:
        if value not in hash_table:
            print('False')
            return False
    print('True')
    return True


is_subset(['a', 'b', 'c'], ['a', 'b', 'c', 'd'])

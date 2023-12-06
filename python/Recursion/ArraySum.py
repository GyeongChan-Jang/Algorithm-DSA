test = [1, 2, 3, 4, 5]


def ArraySum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + ArraySum(arr[1: len(arr)])


answer = ArraySum(test)
print(answer)
# print(test[1: len(test)])

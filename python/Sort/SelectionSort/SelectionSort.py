def selectionSort(list):
    for i in range(len(list) - 1):
        lowestNumberIndex = i
        for j in range(i+1, len(list)):
            if list[j] < list[lowestNumberIndex]:
                lowestNumberIndex = j
        if (lowestNumberIndex != i):
            (list[i], list[lowestNumberIndex]) = (
                list[lowestNumberIndex], list[i])

    return list


selectionSort([3, 5, 2, 65, 5, 3, 1, 23, 2])

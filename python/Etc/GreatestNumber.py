def greatestNumber(array):
    greatestSoFar = array[0]
    for i in array:
        if i > greatestSoFar:
            greatestSoFar = i
    print(greatestSoFar)
    return greatestSoFar


greatestNumber([3, 5, 6, 2, 3, 4, 6, 7])

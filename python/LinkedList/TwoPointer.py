# 완전탐색 O(n^2)
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False


print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))

# 투포인터 O(nlogn)


def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums-1)

    while (l < r):
        if target > nums[l] + nums[r]:
            r -= 1
        elif target < nums[l] + nums[r]:
            l += 1
        else:
            return True
    return False


twoSum

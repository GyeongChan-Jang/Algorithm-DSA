# Dictionary의 key 값은 아무리 많아도 O(1)으로 검색 가능
target = 14
nums = [14, 1, 9, 7, 5, 4, 16]


def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = 1

    for v in nums:
        needed_number = target - v
        # in이 핵심! -> 시간복잡도 O(1), if needed_number in nums -> O(n)
        if needed_number in memo and needed_number != v:
            return True
    return False


two_sum(nums, target)

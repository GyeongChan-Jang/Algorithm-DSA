# Permutation
def permute(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    ans = []
    backtrack([])
    return ans


nums = [1, 2, 3, 4]

permute(nums)

def longestConsecutive(nums):
    longest = 0
    num_dict = {}
    for num in nums:
        num_dict[num] = True  # num_dict = set(nums) - 딕셔너리와 로직 동일
    for num in num_dict:
        if num - 1 not in num_dict:
            cnt = 1
            target = num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    print(longest)
    return longest


longestConsecutive([6, 7, 100, 5, 4, 4])

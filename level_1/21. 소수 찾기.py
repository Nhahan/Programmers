def solution(n):
    nums = [True for i in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 2):
        if nums[i]:
            for k in range(i * i, len(nums), i):
                nums[k] = False
    return nums.count(True) - 2
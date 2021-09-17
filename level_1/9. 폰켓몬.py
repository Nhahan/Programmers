def solution(nums):
    max_get = len(nums) // 2
    species = len(set(nums))
    return max_get if species >= max_get else species
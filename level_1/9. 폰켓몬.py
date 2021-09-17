def solution(nums):
    max_get = len(nums) // 2
    species = len(set(nums))
    return min(max_get, species)
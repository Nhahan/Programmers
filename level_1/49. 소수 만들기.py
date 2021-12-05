import math
from itertools import combinations


def solution(nums):
    primes = is_prime_num(max(nums))
    combs = set([sum(i) for i in combinations(nums, 3) if sum(i) in is_prime_num(max(nums))])
    return len(combs)


def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n) + 1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i * j] = False
                j += 1

    return [i for i in range(len(arr)) if arr[i] == True]

print(solution([1,2,7,6,4]))
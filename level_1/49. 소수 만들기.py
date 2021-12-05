import math
from itertools import combinations

def solution(nums):
    primes = is_prime_num(max(nums))
    return len([i for i in combinations(nums, 3) if i in primes])

def is_prime_num(n):
    arr = [True] * (n + 1)

    for i in range(2, int(math.sqrt(n) + 1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i * j] = False
                j += 1

    return arr

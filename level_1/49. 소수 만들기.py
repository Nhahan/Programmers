import math
from itertools import combinations


def solution(nums):
    possible_list = [sum(i) for i in combinations(nums, 3)]
    primes = is_prime_num(max(possible_list))
    combs = set([i for i in possible_list if i in primes])
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

    return [i for i in range(len(arr)) if arr[i] is True]
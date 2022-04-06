def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if len(divisor(i)) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


def divisor(num):
    divisor_list = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisor_list.append(i)
    divisor_list.append(num)
    return divisor_list

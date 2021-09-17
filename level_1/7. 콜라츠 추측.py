def solution(num):
    count = 0
    while num != 1:
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        count += 1
    answer = count if count < 500 else -1
    return answer
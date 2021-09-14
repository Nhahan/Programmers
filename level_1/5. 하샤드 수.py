def solution(num):
    answer_num = 0
    for n in str(num):
        answer_num += int(n)
    return True if num % answer_num == 0 else False
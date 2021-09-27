def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = list(s)[len(s) // 2 - 1] + list(s)[len(s) // 2]
    else:
        answer = list(s)[len(s) // 2]
    return answer
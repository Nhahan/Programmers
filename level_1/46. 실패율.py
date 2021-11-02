def solution(N, stages):
    total = len(stages)
    answer = []
    for i in range(1, N + 1):
        if i in stages:
            answer.append(stages.count(i))
        total - stages.count(i)
    return answer

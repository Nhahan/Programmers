def solution(d, budget):
    d.sort()
    answer = []
    for i in d:
        if sum(answer) + i <= budget:
            answer.append(i)
        else:
            break
    return len(answer)

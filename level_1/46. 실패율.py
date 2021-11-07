def solution(N, stages):
    failure = [0] * N

    for i in range(1, N + 1):
        total = len([x for x in stages if x >= i])
        fail = stages.count(i)
        if total == 0: break
        failure[i - 1] = fail / total

    li = []
    for i, v in enumerate(failure):
        li.append((v, i + 1))
    result = sorted(li, key=lambda x: (x[0], -x[1]), reverse=True)
    result = [i[1] for i in result]

    return result

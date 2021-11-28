def solution(n, lost, reserve):
    answer = n - len(lost)
    left = [i for i in range(1, n + 1)]
    left.sort()
    reserve.sort()

    for i in reserve:
        left.append(i)
    for i in lost:
        left.remove(i)
    left.sort()
    repetition = []
    for i in set(left):
        if left.count(i) == 2:
            repetition.append(i)
    for i in repetition:
        if left.count(i) == 2:
            if i == 1:
                if i + 1 not in left:
                    left.append(i + 1)
                    answer += 1
            elif i != n:
                if i - 1 not in left:
                    left.append(i - 1)
                    answer += 1
                elif i + 1 not in left:
                    left.append(i + 1)
                    answer += 1
            else:
                if i - 1 not in left:
                    left.append(i - 1)
                    answer += 1
    return answer


print(solution(5, [2, 4], [1, 3, 5]))

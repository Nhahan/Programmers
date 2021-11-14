def solution(n, lost, reserve):
    students = [i for i in range(1, n + 1) if i not in lost]

    for i in reserve:
        if i - 1 >= 1 and i - 1 in lost:
            reserve.remove(i)
            lost.remove(i - 1)
            students.append(i - 1)
        elif i in lost:
            reserve.remove(i)
            lost.remove(i)
            students.remove(i)
        elif i + 1 in lost:
            reserve.remove(i)
            lost.remove(i + 1)
            students.append(i + 1)

    return len(students)


print(solution(5, [2, 4], [1, 3, 5]))

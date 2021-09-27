def solution(n, arr1, arr2):
    def fill0(a, n):
        while len(a) < n:
            if len(a) <= n:
                a = "0" + a
        return a

    answer = []
    c = ""
    for i in range(n):
        a = bin(arr1[i])[2:]
        b = bin(arr2[i])[2:]

        a = fill0(a, n)
        b = fill0(b, n)

        for j in range(n):
            if int(a[j]) + int(b[j]) == 0:
                c = c + " "
            else:
                c = c + "#"
        answer.append(c[-n:])

    return answer
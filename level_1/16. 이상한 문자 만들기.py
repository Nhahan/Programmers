def solution(s):
    answer = ""
    a = s.split(" ")
    for i in range(len(a)):
        if i > 0:
            answer = answer + " "
        for j in range(len(a[i])):
            if j % 2 == 0:
                answer = answer + a[i][j].upper()
            else:
                answer = answer + a[i][j].lower()
    return answer
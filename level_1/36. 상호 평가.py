def solution(scores):
    answer = ''
    eachScore = {}
    for i in range(len(scores)):
        eachScore[i] = []

    for score in scores:
        for i in range(len(score)):
            eachScore[i].append(score[i])

    for i in range(len(scores)):
        max_num = max(eachScore[i])
        min_num = min(eachScore[i])
        my_num = eachScore[i][i]
        if eachScore[i].count(max_num) == 1 and my_num == max_num:
            eachScore[i].remove(my_num)
        elif eachScore[i].count(min_num) == 1 and my_num == min_num:
            eachScore[i].remove(my_num)
        avg = sum(eachScore[i]) // len(eachScore[i])
        if avg < 50:
            answer += "F"
        elif 50 <= avg < 70:
            answer += "D"
        elif 70 <= avg < 80:
            answer += "C"
        elif 80 <= avg < 90:
            answer += "B"
        else:
            answer += "A"

    return answer
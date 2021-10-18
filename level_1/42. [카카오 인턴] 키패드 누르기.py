def co(arr, last_hand, number):
    for i in range(4):
        for j in range(3):
            if number == arr[i][j]:
                last_hand = [i, j]
    return last_hand


def solution(numbers, hand):
    arr = [[0] * 3 for _ in range(4)]
    num = []
    answer = ""
    answers = []
    last_l = [3, 0]
    last_r = [3, 2]
    for i in range(4):
        for j in range(3):
            arr[i][j] = i * 3 + j + 1
    arr[3][1] = 0

    for number in numbers:

        if number % 3 == 1:
            answers.append("L")
            last_l = co(arr, last_l, number)
        elif number % 3 == 0 and number != 0:
            answers.append("R")
            last_r = co(arr, last_r, number)
        else:
            num = co(arr, num, number)
            if abs(last_l[0] - num[0]) + abs(last_l[1] - num[1]) > abs(last_r[0] - num[0]) + abs(last_r[1] - num[1]):
                answers.append("R")
                last_r = co(arr, last_r, number)
            elif abs(last_l[0] - num[0]) + abs(last_l[1] - num[1]) < abs(last_r[0] - num[0]) + abs(last_r[1] - num[1]):
                answers.append("L")
                last_l = co(arr, last_l, number)
            else:
                if hand == "left":
                    answers.append("L")
                    last_l = co(arr, last_l, number)
                elif hand == "right":
                    answers.append("R")
                    last_r = co(arr, last_r, number)
    for i in range(len(answers)):
        answer = answer + answers[i]
    return str(answer)

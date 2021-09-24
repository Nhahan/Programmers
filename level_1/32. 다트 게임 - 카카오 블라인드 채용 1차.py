def solution(dartResult):
    answer = [0, 0, 0]
    scores = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!"]
    sdt = ["S", "D", "T"]
    dartResult = dartResult.replace("10", "!")
    idx = -1
    for s in dartResult:
        if s in scores:
            idx += 1
            answer[idx] += int(s) if s != "!" else 10
        elif s in sdt:
            if s == "S":
                answer[idx] = answer[idx] ** 1
            elif s == "D":
                answer[idx] = answer[idx] ** 2
            elif s == "T":
                answer[idx] = answer[idx] ** 3
        else:
            if idx == 0 and s == "*":
                answer[idx] = answer[idx] * 2
            elif s == "*":
                answer[idx - 1] = answer[idx - 1] * 2
                answer[idx] = answer[idx] * 2
            elif s == "#":
                answer[idx] = answer[idx] * -1
    return sum(answer)

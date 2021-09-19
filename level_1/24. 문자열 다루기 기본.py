def solution(s):
    for i in range(len(s)):
        if s[i].isdigit() == False:
            answer = False
            break
        elif len(s) == 4 or len(s) == 6:
            answer = True
        else:
            answer = False

    return answer
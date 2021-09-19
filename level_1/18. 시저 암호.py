def solution(string, n):
    answer_list = []
    for s in list(string):
        print(s)
        if 97 <= ord(s) <= 122:
            if ord(s) + n > 122:
                answer_list.append(chr(ord(s) + n - 26))
            else:
                answer_list.append(chr(ord(s) + n))
        elif 65 <= ord(s) <= 90:
            if ord(s) + n > 90:
                answer_list.append(chr(ord(s) + n - 26))
            else:
                answer_list.append(chr(ord(s) + n))
        else:
            answer_list.append(" ")
    return "".join(answer_list)
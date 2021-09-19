def solution(string):
    s_list = sorted([ord(s) for s in list(string)], reverse=True)
    return "".join([chr(s) for s in s_list])
def solution(s):
    low = s.lower()
    return True if low.count("p") == low.count("y") else False
def solution(n):
    div = [n]
    for i in range(1, n//2 + 1):
        if n % i == 0:
            div.append(i)
    return sum(div)
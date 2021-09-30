def solution(price, money, count):
    total = 0
    for _ in range(count):
        total += price
    if total > money:
        return total - money
    else:
        return 0
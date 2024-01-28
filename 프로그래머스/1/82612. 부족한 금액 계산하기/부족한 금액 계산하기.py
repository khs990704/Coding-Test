def solution(price, money, count):
    answer = 0
    n = 0
    for i in range(count):
        n += (i+1) * price
    answer = n - money
    if answer < 0:
        answer = 0
    return answer
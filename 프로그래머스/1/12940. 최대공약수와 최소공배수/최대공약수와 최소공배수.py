def solution(n, m):
    answer = []
    x = 0
    for i in range(1, m+1):
        if n % i == 0 and m % i == 0 and x < i:
            x = i
    answer.append(x)
    for j in range(m, 1000000):
        if j % n == 0 and j % m == 0:
            answer.append(j)
            break
    return answer
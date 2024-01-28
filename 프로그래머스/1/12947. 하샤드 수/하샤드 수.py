def solution(x):
    answer = True
    n = list(str(x))
    n = map(int, n)
    if x % sum(n) == 0:
        pass
    else:
        answer = False
    return answer
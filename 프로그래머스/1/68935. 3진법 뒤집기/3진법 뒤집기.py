def solution(n):
    answer = 0
    rest_list = []
    while True:
        n, rest = divmod(n, 3)
        rest_list.append(rest)
        if n == 0:
            break
    answer = sum([i * 3 **idx for idx, i in enumerate(reversed(rest_list))])
    return answer
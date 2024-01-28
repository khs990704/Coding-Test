def solution(n):
    answer = 0
    num_list = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num_list:
            num_list -= set(range(i*2, n+1, i))
    answer = len(num_list)
    return answer
def solution(arr, divisor):
    answer = []
    cnt = 0
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            cnt += 1
    if cnt == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer
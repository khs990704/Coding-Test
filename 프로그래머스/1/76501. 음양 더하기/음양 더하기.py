def solution(absolutes, signs):
    answer = 0
    for i, j in zip(signs, absolutes):
        if i == True:
            answer += j
        else:
            answer -= j
    return answer
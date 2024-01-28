def solution(k, m, score):
    answer = 0
    score = list(sorted(score))
    for i in range(len(score)//m):
        box = []
        box = score[-m:]
        del score[-m:]
        answer += min(box) * m
    return answer
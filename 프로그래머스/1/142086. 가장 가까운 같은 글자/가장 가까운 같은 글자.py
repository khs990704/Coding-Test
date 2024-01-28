def solution(s):
    answer = []
    alpha = []
    for i, c in enumerate(s):
        if c not in alpha:
            alpha.append(c)
            answer.append(-1)
        else:
            alpha.reverse()
            answer.append(alpha.index(c)+1)
            alpha.reverse()
            alpha.append(c)
    return answer
def solution(dartResult):
    answer = []
    bonus = {'S':1, 'D':2, 'T':3}
    score = ''
    
    for i in dartResult:
        if i.isdigit():
            score += i
        elif i in bonus:
            answer.append(int(score)**bonus[i])
            score = ''
        elif i == '#':
            answer[-1] *= -1
        else:
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
            
    return sum(answer)
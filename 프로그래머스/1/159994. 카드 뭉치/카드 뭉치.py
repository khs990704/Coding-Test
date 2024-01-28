def solution(cards1, cards2, goal):
    answer = 'Yes'
    for s in goal:
        if len(cards1) != 0 and s == cards1[0]:
            cards1.remove(cards1[0])
            continue
        elif len(cards2) != 0 and s == cards2[0]:
            cards2.remove(cards2[0])
            continue
        else:
            answer = 'No'
    return answer
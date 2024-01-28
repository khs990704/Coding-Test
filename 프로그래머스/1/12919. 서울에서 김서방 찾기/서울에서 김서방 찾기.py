def solution(seoul):
    answer = 0
    for i in seoul:
        if i != 'Kim':
            answer += 1
        else:
            break
    return "김서방은 " + str(answer) + "에 있다"
def solution(num):
    answer = 0
    for i in range(500):
        if i == 499:
            num != 1
            answer = -1
        if num == 1:
            answer = i
            break
        else:    
            if num % 2 == 0:
                num /= 2
            else:
                num *= 3
                num += 1
    return answer
def solution(number, limit, power):
    answer = 0
    for n in range(1, number+1):
        cnt = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                cnt += 2
        if n**0.5 % 1 == 0:
            cnt -= 1
        if cnt <= limit:
            answer += cnt
        else:
            answer += power
    return answer
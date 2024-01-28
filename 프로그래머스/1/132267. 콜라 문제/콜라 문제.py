def solution(a, b, n):
    answer = 0
    while True:
        if n >= a:
            coke = (n//a) * b
            emp_coke =  a * (n//a)
            answer += coke
            n = n + coke - emp_coke
        else:
            return answer
            break
def solution(n, m, section):
    answer = 1
    start = section[0]
    for loc in section:
        if start + (m-1) < loc:
            start = loc
            answer += 1
    return answer
def solution(s):
    answer = 0
    first = ''
    f_cnt = 0
    n_cnt = 0
    for i in s:
        if first == '':
            f_cnt += 1
            first = i
            continue
        if first == i:
            f_cnt += 1
        else:
            n_cnt += 1
        if f_cnt == n_cnt:
            f_cnt = 0
            n_cnt = 0
            first = ''
            answer += 1
    if first != '':
        answer += 1
    return answer
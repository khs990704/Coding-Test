def solution(s, skip, index):
    answer = ''
    alp = sorted(set('abcdefghijklmnopqrstuvwxyz') - set(skip))
    alp_num = len(alp)
    
    for s_alp in s:
        answer += alp[(alp.index(s_alp) + index) % alp_num]
    return answer
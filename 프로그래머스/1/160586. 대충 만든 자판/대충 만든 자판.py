def solution(keymap, targets):
    answer = []
    alp_key = dict()
    
    for s in keymap:
        for idx, alp in enumerate(s):
            if (alp in alp_key) and (idx+1) > alp_key[alp]:
                continue
            alp_key[alp] = idx + 1
        
    for t in targets:
        cnt = 0
        for alp in t:
            if alp in alp_key:
                cnt += alp_key[alp]
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer
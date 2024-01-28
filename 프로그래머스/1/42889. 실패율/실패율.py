def solution(N, stages):
    answer = []
    n_stage = {}
    chal_num = len(stages)
    for i in range(1, N+1):
        if chal_num != 0:
            fail_num = stages.count(i)
            n_stage[i] = fail_num / chal_num
            chal_num -= fail_num
        else:
            n_stage[i] = 0
    
    answer = sorted(n_stage, key=lambda x:n_stage[x], reverse=True) # 이미 스테이지 순으로 낮은 스테이지 앞에 오도록 되어 있음
    
    return answer
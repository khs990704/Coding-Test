def solution(k, score):
    answer = []
    score_list = []
    for i in score:
        if len(score_list) != k:
            score_list.append(i)
        else:
            if i > min(score_list):
                score_list.remove(min(score_list))
                score_list.append(i)
        answer.append(min(score_list))
    return answer
def solution(answers):
    answer = []
    n_1 = [1, 2, 3, 4, 5] * 2000
    n_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    n_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    cnt_list = []
    for idx, answer_list in enumerate([n_1, n_2, n_3]):
        cnt = 0
        for i in range(len(answers)):
            if answers[i] == answer_list[i]:
                cnt += 1
        cnt_list.append(cnt)
    max_index = list(filter(lambda x: cnt_list[x] == max(cnt_list), range(len(cnt_list))))
    for idx in max_index:
        answer.append(idx+1)
    return answer
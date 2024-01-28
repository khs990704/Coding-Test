def solution(food):
    answer = ''
    food_list = []
    food = list(map(str, food))
    for idx, i in enumerate(food):
        if idx == 0:
            pass
        else:
            for _ in range(int(i) // 2):
                food_list.append(str(idx))
                
    re_food_list = list(reversed(food_list))
                
    str_1 = ''.join(food_list)
    str_2 = ''.join(re_food_list)
    answer = str_1 + '0' + str_2
    return answer
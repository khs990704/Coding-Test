def solution(array, commands):
    n_list = []
    answer = []
    for cmd in commands:
        n_list = array[cmd[0]-1:cmd[1]]
        n_list.sort()
        answer.append(n_list[cmd[2]-1])
    return answer
def solution(s):
    answer = []
    num_alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    alpha = ''
    for a in s:
        if a.isdigit():
            answer.append(str(a))
        else:
            alpha += a
            if alpha in num_alpha:
                answer.append(str(num_alpha.index(alpha)))
                alpha = ''
    answer = int("".join(answer))
    return answer
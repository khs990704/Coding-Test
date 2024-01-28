def solution(sizes):
    answer = 0
    width = 0
    height = 0
    for case in sizes:
        case.sort(reverse=True)
    for case in sizes:
        if width <= case[0]:
            width = case[0]
        if height <= case[1]:
            height = case[1]
    answer = width * height
    return answer
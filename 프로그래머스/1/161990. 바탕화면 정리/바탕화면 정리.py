def solution(wallpaper):
    answer = []
    x_loc = []
    y_loc = []
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                x_loc.append(x)
                y_loc.append(y)
    answer.append(min(y_loc))
    answer.append(min(x_loc))
    answer.append(max(y_loc)+1)
    answer.append(max(x_loc)+1)
    return answer
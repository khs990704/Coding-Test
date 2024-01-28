def solution(name, yearing, photo):
    answer = []
    for pic in photo:
        cnt = 0
        for member in pic:
            for idx in range(len(name)):
                if member == name[idx]:
                    cnt += yearing[idx]
        answer.append(cnt)
    return answer
def solution(arr):
    answer = []
    a = arr[0]
    answer.append(a)
    for i in range(len(arr)-1):
        if arr[i+1] == a:
            pass
        else:
            a = arr[i+1]
            answer.append(a)
    return answer
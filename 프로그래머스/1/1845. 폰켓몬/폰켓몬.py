from collections import Counter

def solution(nums):
    answer = 0
    cnt = Counter(nums)
    if len(cnt) >= len(nums) / 2:
        answer = len(nums) / 2
    else:
        answer = len(cnt)
    return answer
def primenumber(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for idx_1 in range(0, len(nums[:-2])):
        num = 0
        for idx_2 in range(idx_1+1, len(nums[:-1])):
            for idx_3 in range(idx_2+1, len(nums)):
                num = nums[idx_1] + nums[idx_2] + nums[idx_3]
                if primenumber(num) == True:
                    answer += 1
    return answer
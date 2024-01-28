def solution(n, arr1, arr2):
    answer = []
    bin_codes = []
    for i in range(len(arr1)):
        c = bin(arr1[i] | arr2[i])
        c = c[2:]
        if len(c) != n:
            c = '0' * (n-len(c)) + c
        bin_codes.append(c)
    for codes in bin_codes:
        cd = ''
        for code in codes:
            if code == '0':
                cd += ' '
            else:
                cd += '#'
        answer.append(cd)
    return answer
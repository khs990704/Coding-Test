def solution(s, n):
    answer = ''
    for alp in s:
        if alp == ' ':
            answer += ' '
        elif alp.islower():
            answer += chr(ord('a') + ((ord(alp)-ord('a') + n) % 26))
        elif alp.isupper():
            answer += chr(ord('A') + ((ord(alp)-ord('A') + n) % 26))
    return answer
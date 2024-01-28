def solution(s):
    answer = ''
    words = s.split(' ')
    for idx, word in enumerate(words):
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        if idx != (len(words)-1):
            answer += ' '
    return answer
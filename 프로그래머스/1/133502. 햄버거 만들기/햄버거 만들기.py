def solution(ingredient):
    current_ing = []
    answer = 0
    for ing in ingredient:
        current_ing.append(ing)
        
        if current_ing[-4:] == [1, 2, 3, 1]:
            del current_ing[-4:]
            answer += 1
    return answer
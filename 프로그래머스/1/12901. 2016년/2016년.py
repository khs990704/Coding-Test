def solution(a, b):
    answer = ''
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = 0
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    for month in range(1, a+1):
        if month == a:
            days += b
        else:
            if month in days_31:
                days += 31
            elif month in days_30:
                days += 30
            elif month == 2:
                days += 29
    answer = week[(days%7-1)]
    return answer
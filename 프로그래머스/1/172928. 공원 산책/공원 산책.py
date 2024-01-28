def start_loc(park):
    for y_loc, y in enumerate(park):
        if 'S' in y:
            return [y_loc, y.index('S')]
    return [-1, -1]

def move_loc(dog_loc, direction, distance, park):
    s_y, s_x = dog_loc
    y, x = dog_loc
    
    for i in range(distance):
        one_move = [a+b for a, b in zip(dog_loc, direction)]
        y, x = one_move
    
        try:
            if(park[y][x] != 'X') and (0 <= y < len(park)) and (0 <= x < len(park[0])):
                dog_loc = [y, x]
            else:
                return [s_y, s_x]
        except IndexError:
            return [s_y, s_x]
    return [y, x]

def solution(park, routes):
    dog_loc = start_loc(park)
    direction = {'E':[0, 1], 'W':[0, -1], 'S':[1, 0], 'N':[-1, 0]}
    
    for route in routes:
        move_direction = direction[route[0]]
        move_distance = int(route[2])
        
        dog_loc = move_loc(dog_loc, move_direction, move_distance, park)
    return dog_loc
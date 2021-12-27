import math

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"


answer = ''
pad = {1 : (0,0), 2 : (1,0), 3: (2,0),
        4 : (0,-1), 5 : (1,-1), 6 : (2,-1),
        7 : (0,-2), 8 : (1,-2), 9 : (2,-2),
        "*" : (0,-3), 0 : (1,-3), "#" : (2,-3)}
left = "*"
right = "#"

for number in numbers:
    if number == 1 or number == 4 or number == 7:
        left = number
        answer = answer + "L"
    elif number == 3 or number == 6 or number == 9:
        right = number
        answer = answer + "R"
    else :
        num_x =pad.get(number)[0]
        num_y =pad.get(number)[1]
        l_x =pad.get(left)[0]
        l_y =pad.get(left)[1]
        r_x =pad.get(right)[0]
        r_y =pad.get(right)[1]
        
        l_d = math.ceil(math.sqrt(math.pow(num_x - l_x,2) + math.pow(num_y - l_y,2)))
        r_d = math.ceil(math.sqrt(math.pow(num_x - r_x,2) + math.pow(num_y - r_y,2)))
        
        if l_d < r_d:
            left = number
            answer = answer + "L"
        elif l_d > r_d:
            right = number
            answer = answer + "R"
        else:
            if hand == "left":
                left = number
                answer = answer + "L"
            else :
                right = number
                answer = answer + "R"

print( answer )
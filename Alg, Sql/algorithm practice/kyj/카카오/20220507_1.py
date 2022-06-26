def Deploy(case,choice):
    c1 = case[0]
    c2 = case[1]
    if 	choice == 1:    return (c1,3)
    elif choice == 2:    return (c1,2)
    elif choice == 3:    return (c1,1)
    elif choice == 4:    return (c1,0)
    elif choice == 5:    return (c2,1)
    elif choice == 6:    return (c2,2)
    else:   return (c2,3)

def solution(survey, choices):
    answer = ''
    typ = {'R' : 0,'T' : 0,'C' : 0,'F' : 0,'J' : 0,'M' : 0,'A' : 0,'N' : 0}
    for case,choice in zip(survey,choices):
        c,s = Deploy(case,choice)
        typ[c] += s

    keys = list(typ.keys())
    values = list(typ.values())
    for i in range(0,8,2): 
        if values[i] < values[i+1]: answer += keys[i+1]
        else: answer += keys[i]

    return answer

#통과
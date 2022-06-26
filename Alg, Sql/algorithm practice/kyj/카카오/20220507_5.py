def ShiftRow(li):
    temp = li[-1]
    for i in range(len(li)-1,0,-1):
        li[i] = li[i-1]
    li[0] = temp
    return li

def Rotate(li):
    x1,y1,x2,y2 = 0,0,len(li)-1,len(li[0])-1
    start = li[x1][y1]
    min_ = start
    #y1고정
    for i in range(x1,x2):
        li[i][y1] = li[i+1][y1]
    #x2고정
    for i in range(y1,y2):
        li[x2][i] = li[x2][i+1]
    #y2고정
    for i in range(x2,x1,-1):
        li[i][y2] = li[i-1][y2]
    #x1고정
    for i in range(y2,y1,-1):
        li[x1][i] = li[x1][i-1]
    li[0][1] = start
    return li

def solution(rc, operations):
    for o in operations:
        if o == "Rotate":   rc =  Rotate(rc)
        else:   rc = ShiftRow(rc)
    return rc
#효율성 통과 못함
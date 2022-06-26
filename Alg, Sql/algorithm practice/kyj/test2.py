li = [[[1, 0, 12, 4], [2, 9, 0, 15]], [[3, 11, 13, 5], [6, 14, 10, 2]]]
while 1:
    for c in range(len(li)):
        for r in range(len(li[0])):
            if 0 in li[c][r]:   
                print(0)
                break
    else:   
        print(1)
        break

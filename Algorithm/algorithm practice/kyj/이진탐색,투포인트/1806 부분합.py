def partial_sum(): 
    n,s = map(int, input().split())
    seq = list(map(int, input().split()))

    p1 ,p2 , temp= 0, 0 ,0
    answer = 1000000001

    while (1) :
        if temp >= s:
            if p1 == p2:
                print(1)
                exit()
            temp -= seq[p1]
            answer = min(answer, p2 - p1)
            p1 += 1
        
        elif p2 == n:
            break
        else:
            temp += seq[p2]
            p2 += 1
            
    if answer == 1000000001:
        print(0)
    else:
        print(answer)

partial_sum()
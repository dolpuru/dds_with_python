X , Y = map(int, input().split())
Z = (Y*100)//X


if Z>=99:
    print("-1")
else : 
    fst = 0
    end = 1000000000
    while fst <= end:
        mid = (fst + end) // 2
        X_ex = X + mid
        Y_ex = Y + mid 
        Z_ex = (Y_ex*100)//X_ex
        if Z_ex > Z :
            end = mid - 1
        else : 
            fst = mid + 1
    print(end + 1)
    
# Y/X * 100 으로 했었는데 안됐음 
#BUT (Y*100)//X 로 하니까 됨. 
#==> python 부동소수점 오차가 나서 정확하지 않음. 따라서 아래 경우를 써야함.

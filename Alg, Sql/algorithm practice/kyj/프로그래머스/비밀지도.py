n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


answer = []
arr1_ = []
arr2_ = []
for i in range(n):
    arr1_.append(str(bin(arr1[i])[2:])[::-1])
    arr2_.append(str(bin(arr2[i])[2:])[::-1]) 

for i in range(n):
    if len(arr1_[i]) != n:
        temp = n- len(arr1_[i])
        for j in range(temp):
            arr1_[i] += "0"

    if len(arr2_[i]) != n:
        temp = n- len(arr2_[i])
        for j in range(temp):
            arr2_[i] += "0"

for i in range(n):
    line = []
    for j in range(n):
        if arr1_[i][j] == "1" or arr2_[i][j] == "1" :
            line.append('#')
        elif arr1_[i][j]== "0" and arr2_[i][j] == "0":
            line.append(" ")

    answer.append("".join(line[::-1]))

    
print( answer )
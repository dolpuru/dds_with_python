numbers =[4, 1, 2, 1]	
target = 4

len = len(numbers)
count = 0

def dfs(temp, idx):
    if idx >=len:
        if temp == target:  
            global count
            count+=1
        return 
    else:
        dfs(temp+numbers[idx],idx+1)
        dfs(temp-numbers[idx],idx+1)

dfs(0,0)

print(count)



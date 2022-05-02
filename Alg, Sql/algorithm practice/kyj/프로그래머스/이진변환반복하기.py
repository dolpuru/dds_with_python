s = "1111111"

answer = []
z_count = 0
count = 0
while s != '1' :
    z_count += s.count('0')
    count += 1
    s = s.replace("0",'')
    
    
    s = str(bin(len(s))[2:])
    
answer.append(count)
answer.append(z_count) 

print(answer)
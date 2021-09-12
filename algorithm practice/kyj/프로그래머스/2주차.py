def grade(avg):
    if avg >= 90:
        return 'A'
    elif 90 > avg >= 80:
        return 'B'
    elif 80 > avg >= 70:
        return 'C'
    elif 70 > avg >= 50:
        return 'D'
    elif 50 > avg :
        return 'F'

scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
n = len(scores)
answer = ''

self_ = 0
dic = {}
count = 0
for i in range(n): 
    temp = []     #열
    for a,j in enumerate(scores):    #행
        if i == a:
            self_ = j[i]
        else:
            temp.append(j[i])
    if max(temp) >= self_ and min(temp) <= self_:
            temp.append(self_) 

    avg = sum(temp)/len(temp)
    dic[i] = avg
        
for avg in dic.values():
    answer = answer + grade(avg)
    
print(answer)
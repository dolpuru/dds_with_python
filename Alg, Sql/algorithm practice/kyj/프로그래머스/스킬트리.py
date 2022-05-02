skill = "CBD"
skill_trees	= ["BACDE", "CBADF", "AECB", "BDA"]

answer = 0

for i in skill_trees:
    k = 0
    count = 0
    for j in i:
        count += 1
        if skill.find(j) > k:
            break
        elif skill.find(j) == k:
            k += 1
        
    if count ==  len(i):    answer += 1           


print(answer)
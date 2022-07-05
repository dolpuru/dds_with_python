from itertools import combinations
def solution(relation):
    answer = []
    cal = [i for i in range(len(relation[0]))]

    def dis(c,relation):
        nonlocal answer
        cals = []
        set_ = []
        for i in c: cals.append([j[i] for j in relation])

        for i in range(len(relation)):
            temp = []
            for j in range(len(cals)):
                temp.append(cals[j][i])
            set_.append(tuple(temp))
        
        if len(set_) == len(set(set_)): return 1
        else:    return 0

    for i in range(1,len(cal)+1):
        for c in combinations(cal,i):
            if len(answer) == 0:
                if dis(c,relation): answer.append(c)
            else:
                for li in answer:    
                    if set(li).issubset(c): break
                else:    
                    if dis(c,relation): answer.append(c)

    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

# len(temp) = 2
# [['100', '200', '300', '400', '500', '600'],
#  ['music', 'math', 'computer', 'computer', 'music', 
# 'music']]
# temp[k][0]
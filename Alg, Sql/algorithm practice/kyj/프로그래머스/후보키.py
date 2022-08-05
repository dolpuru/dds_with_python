from itertools import combinations
def dis(c,relation):
    cals = [[j[i] for j in relation] for i in c]
    set_ = [tuple(i[j] for j in c) for i in relation]
    if len(set_) == len(set(set_)): return 1
    else:    return 0

def solution(relation):
    answer = []
    cal = [i for i in range(len(relation[0]))]

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

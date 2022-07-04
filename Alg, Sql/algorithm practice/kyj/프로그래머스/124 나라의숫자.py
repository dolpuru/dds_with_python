def solution(n):
    answer = ''
    num = ['1','2','4']

    def country(n):
        q,r = divmod(n,3)
        if q==0: return num[r-1]
        elif q==1 and r==0: return num[2]
        elif r==0:  return country(q-1) + num[2]
        else:   return country(q) + num[r-1]
    return country(n)


print(solution(9))
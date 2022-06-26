s= "abcabcabcabcdededededede"
answer = 0
sliceN = 0
min_ = 1000
for i in range(len(s)):
    sliceN += 1
    temp = s
    before = ''
    count = 0
    answer = ''
    repeat = 0
    while repeat != 2:
        slice_ = temp[:sliceN]
        temp = temp[sliceN:]
        if before =='':
            before = slice_
        elif  before == slice_:
            count+= 1
        else:
            if count == 0:    answer += before
            else:   answer += str(count+1)+before
            before = slice_
            count = 0
        if len(temp) == 0: repeat +=1
    if min_ > len(answer):  min_ = len(answer)
print(min_)

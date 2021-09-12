def solution(answers):
    st_1 = [1,2,3,4,5]
    st_2 = [2,1,2,3,2,4,2,5]
    st_3 = [3,3,1,1,2,2,4,4,5,5]
    
    len_st_1 = len(st_1)
    len_st_2 = len(st_2)
    len_st_3 = len(st_3)
    
    # %를 이용해 계싼해주었다.
    cnt_1, cnt_2, cnt_3 = 0, 0, 0
    for i in range(len(answers)):
        if st_1[ i % len_st_1 ] == answers[i]:
            cnt_1 += 1
        if st_2[ i % len_st_2 ] == answers[i]:
            cnt_2 += 1
        if st_3[ i % len_st_3 ] == answers[i]:
            cnt_3 += 1
    
    temp = [cnt_1, cnt_2, cnt_3]
    answer_list = []
    max_val = (max(cnt_1,cnt_2,cnt_3))
    for i in range(3):
        if max_val == temp[i]:
            answer_list.append(i+1)
    
    return answer_list
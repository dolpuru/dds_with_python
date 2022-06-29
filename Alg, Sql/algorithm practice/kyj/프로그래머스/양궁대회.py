
def solution(n, info):
    answer = [0,0,0,0,0,0,0,0,0,0,0]
    count, a_score, l_score= 0,0,0

    for i in range(10):
        if info[i]: a_score += 10-i
    
    
    
    return answer

answer = [0,0,0,0,0,0,0,0,0,0,0]

# 1. 어피치보다 1개화살 더 많이 쏴서 
# 	어피치점수 - (10-i)
# 	내점수 + 10+i

# 2. 어피치가 쏜 것 피하여 화살을 아낀 후 다른 곳에 쏘기

# 1, 2 번의 경우를 둘다 기술 -> 그래프문제 DFS,BFS 더 나은 것

# 3. 화살이 n 보다 많다면 멈추기

# answer을 추가하면서 info 계속 비교

# 4. 차이 값 max_ 기록하기
import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville) # heapify는 리턴값이 있는게 아님, 그 리스트 형태를 바꿔줌 
        
    answer_cnt = 0
    
    
    while scoville[0] < K:
        min_value = heapq.heappop(scoville)
        
        try:
            min_value2 = heapq.heappop(scoville)   #heapq가 뺄 수 없으니 에러 발생해서, try except 문 사용
            heapq.heappush(scoville, min_value + (2 * min_value2))
            answer_cnt += 1
        except:
            return -1
        
        
    return answer_cnt
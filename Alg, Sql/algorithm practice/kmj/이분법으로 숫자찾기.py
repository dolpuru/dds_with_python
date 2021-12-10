#이분법으로 숫자 찾기
def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list) - 1
    
    if  start_index > end_index:
        return None
        
    mid = (start_index + end_index) // 2
    if some_list[mid] == element:
        return mid 
    elif some_list[mid] > element:
        return binary_search(element,some_list,start_index,mid - 1)
    elif some_list[mid] < element:
        return binary_search(element,some_list,mid + 1,end_index)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
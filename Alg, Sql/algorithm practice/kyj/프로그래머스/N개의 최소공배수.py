def gcd(x,y):
    if y == 0:  return x
    else:   return gcd(y,x%y)

def solution(arr):
    answer = arr[0]

    for n in arr:
        answer = answer*n//gcd(answer,n)
    return answer
    
# 옛날 코드
# def gcd(y,x):
#     if x% y != 0:   gcd(x%y,y)
#     else : return y

# arr = [2,6,8,14]
# lcd_temp = arr[0]
# arr.sort()

# for i in range(len(arr)-1):
#     temp = gcd(lcd_temp,arr[i+1])
#     print(temp)
#     lcd_temp = lcd_temp*arr[i+1] // temp
    
# print( lcd_temp)
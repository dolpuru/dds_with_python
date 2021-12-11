#다른 변수에 함수 할당 가능
def calc_square(digit):
    return digit * digit
calc_square(2)
func1 = calc_square
print(func1)
func1(2)

#함수에 다른 함수에 인자로 넣을 수 있음
def calc_quad(digit):
    return digit * digit * digit * digit
def calc_plus(digit):
    return digit * digit

def list_square(function, digit_list):
    result = list()
    for digit in digit_list:
        result.append(function(digit))
    print(result)
num_list = [1,2,3,4,5]
list_square(calc_square,num_list)
list_square(calc_quad,num_list)
list_square(calc_plus,num_list)

#함수의 결과값으로 함수를 리턴할 수 있음
def loffer(num):
    message = num
    def num_creater():
        print ("high level - ",message)
    return num_creater

log1 = loffer("Dave Log-in")
print(log1)

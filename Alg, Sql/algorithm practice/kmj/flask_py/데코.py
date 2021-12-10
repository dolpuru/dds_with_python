#decorator 함수 정의
def outer_func(function):
    def inner_func():
        print('decoration added')
        function()
    return inner_func

#decorateing할 함수
def log_func():
    print("logging")

#log_func 함수에 inner_func 함수의 기능을 추가한 decorated_func함수
decorated_func = outer_func(log_func)
decorated_func()

#한번에 데코레이터로 작성하면!
@outer_func
def log_func():
    print("logging")
log_func()


#예시 ++
def outer_func(function):
    def inner_func(digit1,digit2):
        if digit2 == 0:
            print("cannot be divided with zero")
            return
        function(digit1,digit2)
    return inner_func

@outer_func
def divide(digit1,digit2):
    print(digit1/digit2)

divide(4,2) #20이 출력된다.
divide(9,0) # cannot be divided with zero이 출력된다

#파라미터와 관계엇이 모든 함수에 적용가능한 decorater
def general_decorater(function):
    def wrapper(*args,**kwargs):
        print("function is decorated")
        return function(*args,**kwargs)
    return wrapper
#*args와 **kwargs를 사용하면 된다.

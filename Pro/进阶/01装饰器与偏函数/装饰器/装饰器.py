


#是一个闭包，把一个函数当做参数，返回一个替代版的函数。本质就是一个返回函数的函数

#简单装饰器：



def func1():
    print("不以物喜，不以己悲")  #定义一个函数，可以打印一行字符串

def onder(func):    #定义一个外部函数
    def inner():    #定义一个内部函数，打印一串字符串
        print("*****")
        func()         #打印完以后还给外部函数的形参
    return inner

f = onder(func1)
f()


# def say(age):
#     print("my age is %d years old" % (age))
#
# say(-10)
#
# def outer(func):
#     def inner(age):  #调用say的形参来判断
#         if age < 0:
#             age = 0
#         func(age) #判断完毕还给outer的形参，
#     return inner
#
#
# sa = outer(say) #把say作为outer的形参
# sa(-10)


# def say(age):
#     print("i am %d years old" % (age))
#
# def outer(func):
#     def inner(age):
#         if age < 0:
#             age = 0
#         func(age)
#     return inner
# f = outer(say)
# f(10)


def say(age):
    print("i am %d year old" % (age))

def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner

all = outer(say)
all(-1)























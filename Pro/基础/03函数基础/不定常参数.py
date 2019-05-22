

"""

概念：能处理比定义时更多的参数





"""


# 加了星号的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元组

def n1(str,*arr):
    print(str)
    for x in arr:
        print(x)

n1("songzi")


def n2(*l):
    sum = 0
    for i in l:
        sum += i
    return sum

print(n2(1,2,3,4,5,6))





# **代表键值对的参数字典，和*所代表的意义类似
def n2(**kwarg):
    print(kwarg)
    print(type(kwarg))

n2(s = 10,o = 20)









def fbook(str,**els):

    print(str,els)
fbook(200,name = "songzi",age = "18")


def car(name,type,money = " "):
    if money:
        print("this car is " + name + type + money)
    else:
        print("this car is " + name + type)
car("baoma","suv")

print(10 % 2)



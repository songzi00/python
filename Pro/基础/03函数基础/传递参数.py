

"""
值传递：传递的是不可变的类型
string,tuple是不可变的


"""

def f1(num):
    num = 100
num2 = 1000
f1(num2)
print(num2)






"""
引用传递：传递的是一个可变的类型
list.dict,set是可变的

"""

def f2(lis):
    lis[0] = 100
li = [1,2,3,4,5]
f2(li)
print(li)







def n1(age):
    age = 18
name = 20
n1(name)
print(name)







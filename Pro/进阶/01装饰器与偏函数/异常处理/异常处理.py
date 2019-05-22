
#当程序遇到问题时不让程序结束，而是越过错误继续向下执行。


"""
try...except...else

格式：
try:
    语句t
except错误表示码 as e:
    语句1
except错误表示码 as e:
    语句2
    ...
except错误表示码 as e:
    语句n
    
else:
    语句e
    
注意：else语句可有可无


作用：用来检测try语句块中的错误，从而让except语句捕获错误信息并处理

逻辑：当程序执行到try-except-else语句时，
1，如果当try"语句t"执行出现错误时，会匹配第一个错误码，如果匹配上
    就执行对应的"语句"
2，如果当try"语句t"执行出现错误，没有匹配的异常，错误将会被提交到上一层的try语句，或者到程序的最上层。
3，如果当try"语句t"执行没有出现错误，那么执行else语句e。（前提是得有else语句）

"""

#第一种
try:
    print(3 / 0)
except ZeroDivisionError as e:
    print("除数为0了")

except NameError as e :
    print("没有该变量")
else:
    print("代码没有问题")



print("%%%%%%%")


#第二种：使用except而不使用任何任何的错误类型
try:
    print(4 / 0 )
except:
    print("程序出现了异常")



#第三种：使用except带着多种异常
try:
    pass
except(NameError,ZeroDivisionError):
    print("出现了NameError,ZeroDivisionError")




#特殊：
#1，


#2，跨越多层调用，main调用了func2，func2调用了func1。func1出现错误，这是只要main捕获到了就可以处理。



def func1(num):
    print(1 / num)
def func2(num):
    func1(num)
def main():
    func2(0)

try:
    main()
except ZeroDivisionError as e:
    print("#####")








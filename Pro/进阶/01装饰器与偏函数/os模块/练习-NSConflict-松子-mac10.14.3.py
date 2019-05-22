




try:
    print(3 % 0)
except ZeroDivisionError as e:
    print("除数为0了")
except NameError as e :
    print("没有该变量")
else:
    print("代码没有问题")


try:
    print(10 / 0)
except:
    print("不管是哪里错了，反正就是有bug")
finally:
    print("111")















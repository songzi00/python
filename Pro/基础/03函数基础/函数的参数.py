
#参数必须按顺序传递，个数要对应。




#形参（形式参数）：定义函数时小括号里面的变量，本质是变量

#实参（实际参数：调用函数时给函数传递的数据，本质是值


            # 形式参数
def fbook(title,name):
    print("one of my favortie books is " + title + name)



fbook("bainian","gudu")
        # 实际参数



def num(num1 = 10,num2 = 20):
    if num1 > num2:
        print("第一个数字大")
    else:
        print("第二个数字大")
num()














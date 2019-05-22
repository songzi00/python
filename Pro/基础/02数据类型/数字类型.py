#导入一个库，
#库：封装一些功能
#math是一个数学相关的库，
#random封装了一些有关随机数的方法
import math
import random


'''

分类：整数、浮点数、复数

'''

'''

整数：python可以处理任意大小的整数，当然包括负整数，在程序中的表示和数学的写法一样

'''

num1 = 10
num2 = num1
print(num2)


#连续定义多个变量
num3, num4, num5 = 1, 1, 1
print(num3, num4, num5)

#交互式复制定义变量
num6, num7 = 6, 7
print(num6, num7)


"""
浮点数：浮点型由整数部分与小数部分组成，浮点数运算可能会有四舍五入的误差
"""

f1 = 1.1
f2 = 2.2
print(f1 + f2)

"""
复数：实数部分和虚数部分构成，可以用a + b
"""
"""
数字类型转换
"""
#转化成整数
print(int(2.2345))
print(int("125"))

#转化为浮点数
print(float(79))
print(float("329"))

#转换时的+、-号只有作为正负数的时候才有效,如有其它字母、数字之间的加减号则无效
print(int("-128"))
print(int("+648"))




















#数学功能

#返回数字绝对值
a1 = -10
a2 = abs(a1)
print(abs(a2))

#比较两个数大小，有两种状态，true可以看做是1，false看作是0
a3 = 100
a4 = 103
print((a3>a4) - (a3<a4))

#返回指定参数的最大值、最小值
print(max(a3, a4))
print(min(a3, a4))

#求x的y次方
print(pow(2, 5))

#四舍五入 (x,n)表示x要舍入到n位数
print(round(8.49))
print(round(3.8578, 3))
print(round(3.45, 1))

#向上取整
print(math.ceil(12.4))
print(math.ceil(12.9))

#向下取整
print(math.floor(12.4))
print(math.floor(12.9))

#返回整数和浮点数部分
print(math.modf(65.8))

#开方
print(math.sqrt(18))

#随机数
#从序列的元素中随机挑选一个元素
print(random.choice(["zhangduoduo", "songzi", "zhangyongshun"]))
print(random.choice(range(5)))

#生成0-100的随机数
r1 = random.choice(range(99)) + 1
print(r1)

#从指定的范围中，从指定的技术递增的集合中选取一个随机数
#random(randrange([start,] stop [, step]  ))
#start--指定范围的开始值，包括在指定的范围内
#stop--指定范围的结束值，不包括在指定的范围内
#step--指定的递增基数

print(random.randrange(1, 100, 2))

#随机生成(0, 1)的随机数(浮点数）
print(random.random())

#将序列的所有元素随机排序
list = [1, 2, 3, 4, 5, 6]
random.shuffle(list)
print(list)

#s随机生成一个实数，在【3, 9】之间，包含3和9
print(random.uniform(3, 9))
import datetime


"""

datatime比time高级很多，可以理解为datatime基于time进行了封装
提供了各位使用的函数，datatime模块的接口更直接，更容易调用


模块中的类：
datatime    同时有时间和日期
timedelta   主要用于计算时间的跨度
tzinfo  时区相关
time    只关注时间
date    只关注日期


"""






# 获取当前时间
d1 = datetime.datetime.now()
print(d1)
print(type(d1))


# 获取指定的时间
d2 = datetime.datetime(2000,11,24,8,20,45,123456)
print(d2)

# 将时间转为字符串
d3 = d1.strftime("%y-%m-%d %x")
print(d3)
print(type(d3))

# 将格式化字符串转为datetime对象
# 转化的格式要与字符串一致
# d4 = datetime.datetime.strptime(d3,"%y-%m-%d %x")
# print(d4)

d5 = datetime.datetime(2000,11,24,8,20,45,123456)
d6 = datetime.datetime.now()
d7 = d6 - d5
print(d7)
print(type(d7))
# 间隔的天数
print(d7.days)
# 间隔天数除外的秒数
print(d7.seconds)


s = "|"
s1 = "*|"

p1 = s + s1
print(p1)

p2 = s + (s1 *2)
print(p2)

p3 = p2 + s1
print(p3)





































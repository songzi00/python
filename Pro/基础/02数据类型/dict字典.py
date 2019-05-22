



"""
概述：
    使用键-值（key：value)存储，具有极快的查找速度


key的特性：
        1，字典中的可以必须唯一
        2，key必须是不可变得对象
        3，字符串、整数等都是不可变得。可以作为key
        4，list是可变的，不能作为key
        5,字典是无序的，

思考：保存多位学生的姓名和成绩

使用字典，学生姓名作为key，学生成绩作为值


"""

# #创建字典
# dict1 = {"songzi":60,"zhangduoduo":70}
#
# #元素访问
#
# #获取：字典名[key]
#
# print(dict1["songzi"])
#
# #添加：
# dict1["zhangyongshun"] = 100
#
# #修改  因为一个key只对应一个value，所以，多次对一个key的value赋值，其实就是修改值
# dict1["songzi"] = 95
#
#
# #删除
# dict1.pop("zhangduoduo")
# dict1["shijian"] = 5
# print(dict1)
#
#
# #遍历
# for key in dict1:
#      print(key)
#
# for value in dict1.values():
#     print(value)
#
# for k,v in dict1.items():
#     print(k,v)
#
# #排序
#
# for i,v2 in enumerate(dict1.values()):
#     print(i,v2)


#和list比较
#1，查找和插入的速度极快，不会随着key和value的增加而变慢
#2，需要占用大量的内存，内存占用很多


#list
#1，查找和插入的速度会随着数据量的增多而减慢。
#2，占用的空间小，浪费内存少




w = "songzi"
d = {}

str = "songzi is nice girl ! songzi is pretty girl ! songzi is good girl !"

l = str.split(" ")


for v in l:
    s = d.get(v)

    if s == None:
        d[v] = 1
    else:
        d[v] += 1

print(d[w])


w = "s"
d = {}
str = "w r t f s f h c a f h r s s s"
for q in str:
    z = d.get(q)
    if z == None:
        d[q] = 1
    else:
        d[q] += 1
print(d)




dict1 = {"songzi":60,"zhangduoduo":70,"dalian":76}

for i,v in enumerate(dict1.values()):
    print(i,v)





# 小练习
#时间下一秒
timestr = input()
timelist = timestr.split(":")

h = int(timelist[0])
m = int(timelist[1])
s = int(timelist[2])

s += 1

if s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0

print("%.2d:%.2d:%.2d" % (h,m,s))

















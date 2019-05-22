
"""
本质：是一个有序集合

特点：
1，与列表非常的相似
2，一旦初始化就不能修改
3，使用小括号


创建元组：
格式：元组名 = （元组元素1，元组元素2，元组元素3。。。）



"""

#创建一个元组

tuple1 = (1,)
print(tuple1)
print(type(tuple1))


#元组元素的访问
#格式：元组名[下标]（下标从0开始）


tuple = (1,4,64,245,785,35,26,5)
print(tuple[3])


#获取最后一个元素
tuple = (1,4,64,245,785,35,26,5)
print(tuple[-1])

#修改元组

tuple2 = (1,2,3,4,[47,88,21,49])
tuple2[-1][2] = 100
print(tuple2)

#删除元组
tuple3 = (1,2,3,4)
#del tuple3
print(tuple3)


#元组操作
tuple4 = (1,2,3)
tuple5 = (4,5,6)
tuple6 = tuple4 + tuple5
print(tuple6)

#元组重复
tuple7 = (1,2,3)
print(tuple7 * 3)

#判断元素是否在元祖
tuple8 = (1,2,3)
print(1 in tuple7)

#元祖的截取

tuple9 = (1,2,3,4,5,6,7)
print(tuple9[3:8])



#二维元组
tuple10 = ((1,2,3),(4,5,6),(7,8,9))
print(tuple10[2][1])



#元组的方法

tuple11 = (1,2,3,4,5,6,7)

#返回元祖的元素个数
print(len(tuple11))

#求元组中元素的最大值和最小值
print(max(tuple11))
print(min(tuple11))

#将列表转成元组
list1 = [1,2,3]
tup1 = tuple(list1)
print(tup1)

#元祖的for语句

for i in (1,2,3,4,5):
    print(i)
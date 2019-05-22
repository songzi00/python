



"""

set;类似dict，是一组key的集合，只存key，不存value.不可以有重复的元素

本质：是无序和无重复的元素的集合



"""

#创建
#创建set需要一个list或者 tuple或者dict作为输入集合
#重复元素在set中会自动过滤

#列表
s1 = set([1,2,3,4,5,9,4,3,5,1])
print(s1)

#元祖
s2 = set((1,2,3,4,5,9,4,3,5,1))
print(s2)

#字典(只获取key)
s3 = set({1:"nice",2:"good"})
print(s3)


#添加(添加重复的元素是没有效果的，字典，列表不可添加，因为可变。元祖可以添加

s4 = set([1,2,3,4,5])
s4.add(7)
print(s4)

#插入整个list、tuple、字符床，打碎插入

s5 = set([1,2,3,4])
s5.update([6,7,8])
s5.update((9,10,11))
s5.update("songzi")
print(s5)


# 删除
s6 = set([1,2,3,4])
s6.remove(3)
print(s6)


#遍历

s7 = (["songzi","is","good","girl"])

for i in s7:
    print(i)

#排序

for i,v in enumerate(s7):
    print(i,v)



s8 = set([1,2,3,4,5])
s9 = set([4,5,6,7,8])


#交集

a1 = s8 & s9
print(a1)


#并集

a2 = s8 | s9
print(a2)



list1 = [12,5,4,645,12,5,99,62,99,10,]
set1 = set(list1)

print(set1)



endstr = "end"

str = ""

for line in iter()

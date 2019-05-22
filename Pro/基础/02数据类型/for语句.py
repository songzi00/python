


"""
格式：

for 变量名 in 集合：
    语句

逻辑：
按顺序取集合中的每个元素赋值给变量，再去执行语句，如此循环往复，直到取完集合中的元素截止




range（start,end,step）函数——生成数列
start默认为0，step默认为1
"""


for x in range(1,10,3):
    print(x)




#同时标注下标与元素

for x,y in enumerate([1,2,3,4,5]):
    print(x,y)


#1+到100的和

sum = 0

for x in range(1,101):
    sum += x
print(sum)


list1 = [1,2,3,4]
n1 = tuple(list1)
print(n1)
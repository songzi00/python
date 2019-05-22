"""
#获取列表的平均值

list = [12,34,56,87,23]
n1 = 0
n2 = 0

while n1 < 3:
    n2 += list[n1]
    n1 += 1

print("平均值 = %d" % (n2 / 5))

list3 = [1,2,3,4]
print(3 in list3)

list5 = [1,2,3,4,5,6,7,8,9]
print(list5[2:5])

list6 = [1,2,3,4,5,6]
list6.insert(3,280)
print(list6)


list7 = [1,2,3,4,5,6,7]
print(list7.pop(2))

list8 = [1,23,45,61,58]
list8.remove(58)
print(list8)




list9 = [1,2,3,4,5,6]
list9.clear()
print(list9)

list10 = [1,2,3,4,5]
list11 = list10.index(4)
print(list11)

list12 = [1,66,37,357,357,2,4,657,34]
print(len(list12))

list13 = [633,456,62,66,4357,686,24,75]
print(min(list13))

list14 = [1,2,3,4,1,3,5,5,6,3,6]
print(list14.count(3))


list15 = [1,2,6,4,6,7,6,4,6]

p = 0
all = list15.count(6)

while p < all:
    list15.remove(6)
    p += 1

    print(list15)




list16 =  [1,2,3,4,5,6]
list16.reverse()
print(list16)


list17 = [2,5,7,3,6,8,9]
list17.sort()
print(list17)


list18 = [1,2,3,4,5,6]
list19 = list18
list19[2] = 36
print(list19,list18)

list20 = [1,2,3,4,5]
list21 = list20.copy()
list21[2] = 49
print(list20,list21)


list = [1,5,3,8,4,6,2,9]

list.sort()

count = list.count(list[len(list) - 2])
c = 0

while c < count:
    list.pop()
    c += 1

print(list[len(list) - 2])

"""


num = int(input())

i = 2

while num != 0:
    if num % i == 0:
        print(i)
        num //= i
    else:i += 1



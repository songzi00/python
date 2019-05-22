

"""
break语句：

作用：跳出for和while循环
注意：break只能跳出离它最近的那一层循环
    循环语句可以有else语句，break导致的 循环截至以后，else语句不会执行


"""


for x in range(10):
    print(x)
    if x == 4:

        break



i = 1

while i <= 10:
    print(i)
    if i == 6:
        break
    i += 1
else:print(123)



"""

概念：调用函数时，如果没有传递参数，那么则使用默认参数




·
"""

# 以后用默认参数，最好将默认参数放在最后
def n1(name  = "songzi",age  = 18):
    print(name,age)

n1("duoduo",20)






num1 = 0
for i in range(101):
    num1 += i
    i += 1
print(num1)


def num2():
    print(sum(range(1,101)))

num2()



def songzi(str):
    c = 0
    for i in str:
        c += 1
    return c

str = input()
print(songzi(str))


sum = 0

for i in range(101):
    sum += i
    i += 1

print(sum)
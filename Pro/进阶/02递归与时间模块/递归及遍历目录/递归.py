

"""
递归调用：一个函数，调用了自身,称为递归函数
方式：
    1，写出临界条件
    2，找出这一次和上一次的关系
    3，假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果





"""


"""
1 + 2 + 3 + 4 + 5 + n
sun[1] + 2 = sum[2]
sun[2] + 3 = sum[3]
sun[3] + 4 = sum[4]
sun[4] + 5 = sum[5]


"""

def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n -1)
res = sum2(10)
print(res)









def s1(n):
    sum = 0
    for x in range(1,n+1):
        sum += x
    return sum

res = s1(10)
print(res)






























#
# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n - 1)
# res = sum(10)
# print(res)
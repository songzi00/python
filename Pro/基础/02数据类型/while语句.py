"""
while语句：

格式：  while表达式：
            语句


逻辑：当程序执行到while语句，首先会计算"表达式"的值，如果"表达式"的值为假，那么结束整个while语句，
如果"表达式"的值为真，则执行"语句"，执行完"语句"再计算"表达式"的值。如果表达式的值为假，那么结束while语句。
如果表达式的值为真，则执行语句，如此循环，直到表达式的值为假才停止。




"""


"""
num = 1
while num <= 5:
      print(num)
      num += 1
"""



"""
sum =0
num = 1
while 1 <=10            num =1 
    sum = sum + num     1 = 0 + 1
    print("sum = %d " %  (1))
    
      2<=10             num =2 
    sum = sum + num     3= 0+1  + 2
    print("sum = %d " %  (3))
    
      3<=10             num =3 
    sum = sum + num     6= （（0+1） + 2）+3
    print("sum = %d " %  (6))
    
      4<=10             num =4 
    sum = sum + num     2= （（（0+1 ） + 2）+3）+4
    print("sum = %d " %  (？))
      5<=10             num =5 
    sum = sum + num     ？？？？
    
      6<=10             num =6
    sum = sum + num     ？？？？？
    
    ……    ……
      

"""


#练习

#1 + 2 + 3直到100

sum = 0
num = 1
while num <= 10:
    sum += num
    num += 1
    print("sum = %d " % (sum))

#单独输出每个字符串的字符

n1 = "zhangduoduo"
n2 = 0

while n2 < len(n1):
    print("你是[%d] = %s" % (n2,n1[n2]))
    n2 += 1

#找出100-999之间的水仙花数
num = 100
while num <= 999:
     a = num % 10
     b = num // 10 % 10
     c = num // 100
     if num == a**3 + b**3 + c**3:
         print(num)
     num += 1

#找出三位数都相同的数'


num = 100
while num <= 999:
    a = num % 10
    b = num // 10 % 10
    c = num // 100
    if a == b == c:
        print(num)
    num += 1


#找出质数（只能被自身和0除尽）
num = int(input())

if num == 2:
    print("是质数")
m1 = 2

while m1 < num:
    if num % m1 == 0:
        print("不是质数")
    m1 += 1

if num == m1:
    print("是质数")



#计算每个数的和

q1 = input()
q2 = 0
q3 = 0

while q2 < len(q1):
    if q1[q2] >= "0" and q1[q2] <= "9":
        sum += int(q1[q2])
    q2 += 1

print("q3 = %d" % (q3))
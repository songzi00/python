"""
if

if else



if-elif-else

格式：

if 表达式1：
    语句1

elif 表达式2：
    语句2
elif 表达式3：
    语句3
elif 表达式4：
    语句4

else：
    语句1


逻辑：当程序执行到if-elif-else时，首先计算表达式1的值，如果表达式1的值为真，那么执行"语句1"，
     执行完"语句1"则跳过整个if-elif-else语句。如果表达式1的值为假，那么计算表达式2的值。
     如果表达式2的值为真，那么执行语句2，然后跳过整个语句。如果表达式2的值为假，那么执行表达式3
     以此类推，直到某个表达式的值为真才停止。
     如果没有表达式的值为真，且有else语句，则执行else语句。


所有的elif都是对它上面所有表达式的否定




"""


n1 = int(input())

if n1 < 18:
    print("未成年")
elif n1 <= 30:
    print("成年")
elif n1 <= 60:
    print("中年")
elif n1 <= 80:
    print("老年")
else:
    print("无法界定")
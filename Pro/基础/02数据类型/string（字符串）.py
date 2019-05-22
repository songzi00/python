"""
什么是字符串？
字符串是以双引号或者单引号扩起来的任何文本,  并且字符串不可变

'阿德'
"张朵朵"

"""

#创建字符串

print("曾经沧海难为水，除却巫山不是云 ")
n2 = "sunck is a good men"
n5 = "sunck is a nice men"



#练习

"""
b7 = int(input("请输入一个年份："))

if (b7 % 4 == 0 and b7 % 100 != 0)or b7 % 400 == 0:
    print("是闰年")
else:print("不是闰年")

"""










"""
字符串运算
"""

#一,字符串连接

n6 = "hello"
n7 = "world"
n8 = n6 + n7
print(n8)

#二，输出重复的字符串
n9 = "me"
n10 = n9 * 3
print(n10)

#三,访问字符串中的某一个字符
#通过索引下标查找字符，索引从零开始
#字符串【下标】

b1 = "sunck is a good men"
print(b1[3])

#(b1[3]) = "34"
#print((b1[3]))   字符串不可变


#四，截取字符串

b2 = "sunck is a good men"
#从给定下标处开始，到给定下标处之前。
b3 = b2[0:8]
print(b3)


#从零开始到给定下标处之前
b4 = b2[:5]
print("b4 = ",b4)

#从给定下标处开始到结尾
b5 = b2[16:]
print("b5 = ",b5)


2
#五,判断字符串

b6 = "my heart will go on"
print("go" in b6)
print ("go1" not in b6)

#六、格式化输出

n7 = 10
n8 = "lang"
n9 = 24.5132868
#占位符——数字占位：%d、字符串：占位%s、浮点数占位：%f（%.3f:保留小数点三位数）

print("n7 = %d, n8 = %s, n9 = %.3f" % (n7,n8,n9))



"""
七、转义字符   \
#将一些字符转换成一个有特殊含义的字符
"""

#1,  转行\n
print("n7 = %d\nn8 = %s\nn9 = %.3f" % (n7,n8,n9))

#2,  \\:将\转换为普通的字符
print("n7 = %d\\nn8 = %s\\nn9 = %.3f" % (n7,n8,n9))

#\'  \"
print('tom is a \'good\' mem')
print("tom is a \"good\" mem")
print("tom is a 'good' mem")

#3,  如果字符串内有很多换行，\n写在一行影响阅读
print("some\npeople\n")
print("""
me
you
he
""")

#4,  \t 制表符(4个空格）
print("some\tfish")

#5， 如果字符中有许多的字符串需要转移，就需要加入好多的\，为了简洁，python允许用r表示内部的字符串默认不转义

#   \\\n\\

print(r"\\\n\\")

"""
windom路径：

c:users\Desktop\python

linux路径：

/root/user/sunck/desktop/python
"""





#6,eval(str)
#功能：将字符串str当成有效的表达式来求值，并返回计算结果。

n10 = eval("350")

print(n10)
print(type(n10))

print(eval("+148"))
print(eval("-148"))
print(eval("14 + 8"))
print(eval("14 - 8"))
#print(eval("14n8"))

#7,len()  返回字符串的长度(字符个数）

print(len("hello world"))


#8,lower（） 将转换字符串中的大写字母为小写字母

n11 = "SUNCK IS A GOOD MEN!"

n12 = n11.lower()
print(n12)
print("n11 = %s" % (n11))


#9,upper () 将转换字符串中的小写字母为大写字母
print("i have a dream".upper())


#10,swapcase（）将字符串中的大写字母转换为小写字母，小写字母转换为大写字母

print("suNCk IS a gooD mEn".swapcase())


#11,capitalize()  将字符串中的首字母转换为大写，其他的小写
print("suNCk IS a gooD mEn".capitalize())


#12,title() 每个单词的首字母大写

print("suNCk IS a gooD mEn".title())


#13,   center(weith,fillchar) 返回一个指定宽度居中的字符串，fillchar为填充的字符串,默认是空格为填充的字符串
n13 = "suNCk IS a gooD mEn"

print(n13.center(80,"$"))



# 14,  ljust(width[,fillchar])返回一个指定宽度的左对齐字符串，fillchar为填充的字符串,默认是空格为填充的字符串
n14 = "suNCk IS a gooD mEn"
print(n14.ljust(40,"$"))




#15   rjust(width[,fillchar])返回一个指定宽度的右对齐字符串，fillchar为填充的字符串,默认是空格为填充的字符串
n15 = "suNCk IS a gooD mEn"
print(n15.rjust(40,"$"))

#16,zfill(width)             返回一个长度为width的字符串，原字符串右对齐，前面的补0
n16 = "suNCk IS a gooD mEn"
print(n16.zfill(40))


#17，count（str[,start][,end]）   返回字符串中指定字符串所出现的次数，可以指定范围，默认从头到尾
n17 = "suNCk IS a  very  very gooD mEn"
print(n17.count("very",15,len(n17)))

#18,小练习
n18 = "怕什么真理无穷，进一寸有进一寸的欢喜"

if n18.count("寸") > 2:
    print("请重新输入")
else:print(n18)


#19， find() find返回的是匹配的第一个字符串的位置,可以指定范围，默认从头到尾。没有返回-1.
n19 = "my name is amy"
print(n19.find("s"))
print(n19.find("s",7,len(n19)))

#20， rfind() find返回的是匹配的最后字符串的位置,可以指定范围，默认从头到尾。没有返回-1.
n20 = "my name is amy"
print(n20.find("s"))



#21, index(str,start,end)    跟find一样的功能，只不过如果str不存在，会回报一个异常
n21 = "怕什么真理无穷，进一寸有进一寸的欢喜"
print(n21.index("一"))


#22, rindex(str,start,end)    跟rfind一样的功能，只不过如果str不存在，会回报一个异常
n22 = "怕什么真理无穷，进一寸有进一寸的欢喜"
print(n22.rindex("一"))


#23， lstrip()会截掉字符串中左侧的指定的字符串，默认为空格
n23 = "*************怕什么真理无穷，进一寸有进一寸的欢喜"
print(n23.lstrip("*"))

#24， rstrip()会截掉字符串中右侧的指定的字符串，默认为空格
n24 = "怕什么真理无穷，进一寸有进一寸的欢喜*************"
print(n24.rstrip("*"))


#25, strip()会截取字符串中两侧的指定字符，默认为空格
n25 = "*************怕什么真理无穷，进一寸有进一寸的欢喜*************"
print(n25.strip("*"))


#26切割字符串：split(str= "",num)以str为分隔符截取字符串，指定num，则只截取num个字符串

n26 = "songzi is a pretty girl"
print(n26.split(" "))


n27 = "i miss zhangduoduo"
n28 = n27.split(" ")
c = 0
for y in n28:
    if len(y) > 0:
        c += 1
print(c)


#27 切割字符串：splitlines([keepends]) 安装（"/r","/n/")分隔
#keepends == ture会保留换行符

n27 = """
少无闲适欲
性本爱丘山
误入尘网中
一去三十年
"""
print(n27.splitlines())




#28 组合列表：join(seq) 以一个指定的字符串分割符，将seq中的所有元素组合成一个字符串

n28 = ['songzi','is','a','pretty','girl']
x28 = " ".join(n28)
print(x28)


#29 求字符串中的大小 max(),min(),最小的是空格
n29 = "songzi is a pretty girl"
print(max(n29))
print(min(n29))

#30 replace(oldstr,newstr,count)替换字符串

n30 = "songzi is a pretty pretty girl"
x30 = n30.replace("pretty","nice",1)
print(n30)
print(x30)


#31 startswith(str,start,end)在给定的范围内判断是否以指定的str开头，如果没有给定范围，默认为整个字符串

n31 = "songzi is nice girl"
print(n31.startswith("songzi"))


#32 endtswith(str,start,end)在给定的范围内判断是否以指定的str结尾，如果没有给定范围，默认为整个字符串

n32 = "songzi is nice girl"
print(n31.endswith("girl"))

#33  编码encode(encoding="utf-8", errors="strict")

n33 = "songzi is a nice girl"
x33 = n33.encode("utf-8")
print(x33)

#34  解码decode(encoding="utf-8", errors="strict")注意：要与编码时的编码格式一致
#ignore 忽略错误
n34 = x33.decode("utf-8")
print(n34)

#35isalpha()
#如果字符串中至少有一个字符且所有的字符都是字母，返回true，否则返回false

n35 = "songzi is a nice girl"
print(n35.isalpha())




#36 isalnum()
#如果字符串中至少有一个字符且所有的字符是数字或者字母，返回true，否则返回false


n36 = "1a23"
print(n36.isalnum())

#37 isupper()
#如果字符串中至少有一个英文字符且所有的英文字符都是大写的英文字符，返回true，否则返回false

n37 = "SONGZI"
print(n37.isupper())


#38 islower()
#如果字符串中至少有一个英文字符且所有的英文字符都是小写的英文字符，返回true，否则返回false

n38 = "songzi"
print(n38.islower())


#39 istitle
#如果字符串是标题化的返回true，否则返回false

n39 = "Songzi Is"
print(n39.istitle())

#40 isdigit()
#如果字符串只包含数字字符返回true，否则返回false

n40 = "1234"
print(n40.isdigit())




#41 如果字符串中只包含空格返回true，否则返回false

n41 = " "
print(n41.isspace())













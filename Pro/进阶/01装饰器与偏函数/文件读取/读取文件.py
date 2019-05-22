"""
过程：
1，打开文件
2，读文件内容
3，关闭文件



"""




"""
1，打开文件：

open(path,flag,[encoding])
path:要打开文件的路径
flag：打开方式
r   以只读的方式打开文件，文件的描述符放在文件的开头
rb  以二进制格式打开一个文件，而且用于只读。文件的描述符放在文件的开头
r+  打开一个文件用于读写，文件的描述放在文件的开头
w   打开一个文件只用于写入，如果该文件已经存在将会覆盖。如果不存在则创建新文件
wb  打开一个文件只用于写入二进制，如果该文件已经存在将会覆盖。如果不存在则创建新文件
w+  打开一个文件用于读写，如果该文件已经存在将会覆盖。如果不存在则创建新文件
a   打开一个文件用于追加，如果文件存在，文件描述符将会放在文件的末尾
a+

encoding:编码方式
errors:错误处理


"""
#ignore:忽略错误
path = r"/Users/oukoto/Desktop/nice.py"

f = open(path,"r",encoding="utf-8")



"""
2，读取文件

"""

# 1、读取文件的全部内容
# str = f.read()
# print(str)

#2读取指定字符（前面的读取了，后面的只能接着前面的取。）
# str1 = f.read(12)
# print(str1)
#
# str2 = f.read(3)
# print(str2)


#3、读取一整行，包括\n字符
# str4 = f.readline()
# print(str4)
#
# str5 = f.readline()
# print(str5)
#
# # #4、读取指定字符数
# # str6 = f.readline(10)
# # print(str6)
#
#
# 5、读取所有行并且返回列表
# list7 = f.readlines()
# print(list7)

#
# # #6、若给定的数字大于0，返回实际size字节的行数
# # list8 = f.readlines(25)
# # print(list8)
#
# print("####")
# # 修改描述符的位置
# f.seek(0)
#
# str9 = f.read()
# print(str9)
#
# # 一个完整的过程
try:
    f1 = open(path,"r",encoding="utf-8")
    print(f1.read())
finally:
    if f1:
        f1.close()

# # with可自动关上文件
with open(path,"r",encoding="utf-8") as f2:
    print(f2.read())
#
#
#
#


"""

3，关闭文件



"""






















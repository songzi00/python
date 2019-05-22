import os


"""
os模块：包含了普遍操作系统功能





"""

# 获取操作系统类型 nt->windows    posix->Linux、Unix或者mac osx
# print(os.name)

# 打印操作系统详细信息（Windows不支持）
# print(os.uname())

# 获取操作系统中的所有环境变量
# print(os.environb)

#获取指定环境变量
# print(os.environ.get("PATH"))

#获得当前目录
# print(os.curdir)

# 获取当前工作目录，即当前python脚本所在的目录
# print(os.getcwd())

#以列表的形式返回指定目录下的所有文件
# print(os.listdir("/Users/oukoto/Desktop/gu"))

#在当前目录下创建新目录
# os.mkdir("songzi")
# os.rmdir("songzi")


# 删除目录
# os.rmdir("songzi")

# 获取文件属性
# print(os.stat("songzi"))

# 重命名
# os.rename("songzi","duoduo")

#删除普通文件
# os.remove("fuxi.py")

#运行shell命令
# os.system("write")写字板
# os.system("mapaint") #画板
# os.system("shutdown-s-t 500")
# os.system("shutdown-a")
# os.system("taskkill /f /im notepad.exe")


# 有些方法存在os模块，还有些存在os.path

# 查看当前的绝对路径
print(os.path.abspath("foryou"))

# 拼接路径
p1 = "/Users/oukoto/Desktop/zhushi"
p2 = "foryou"   #注意：参数2里开始不要有斜杠
p3 = "/root/zhushi/you"
p4 = "foryou"
print(os.path.join(p3,p4))

# 拆分路径
path2 = "/Users/oukoto/Desktop/zhushi"
print(os.path.split(path2))


# 获取扩展名
print(os.path.splitext(path2))


#判断是否是目录
print(os.path.isdir(path2))


# 判断文件是否存在
path3 = r"/Users/oukoto/Desktop/zhushi/输出.py"
print(os.path.isfile(path3))


# 判断目录是否存在
path4 = r"/Users/oukoto/Desktop/zhushi"
print(os.path.exists(path4))


# 获得文件大小(字节）
print(os.path.getsize(path4))


# 获取文件目录
print(os.path.dirname(path4))
# print(os.path.basname(path4))


























































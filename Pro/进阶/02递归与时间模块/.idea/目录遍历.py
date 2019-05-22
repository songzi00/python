import os


# 1，递归遍历目录

def getall(path):  #建立函数
    fileslist = os.listdir(path) # os.liststr()函数：得到当前目录下所有的文件，赋予给变量
    for filename in fileslist:
        if os.path.isdir(os.path.join(path,filename)):
            print("目录： ",filesname)
        else:
            print("文件： ",filename)



    print(fileslist) #打印变量





getall(r"/Users/oukoto/Desktop/gu") #提供路径



#栈模拟遍历
































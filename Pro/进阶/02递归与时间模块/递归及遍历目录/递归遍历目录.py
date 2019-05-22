import os

def get_alldir(path):
    # 得到当前目录下所有的文件
    filelist = os.listdir(path)


    # 处理每一个文件
    for filename in filelist:
        # 判断是否是路径
        fileabs = os.path.join(path,filename)
        if os.path.isdir(fileabs):
            print("目录= ",filename)
            get_alldir(fileabs)
        else:
            print("普通文件= ",filename)




get_alldir(r"/Users/oukoto/Desktop/os")
 

































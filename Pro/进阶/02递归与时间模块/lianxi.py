import os
import collections

def zhan(path):
    filelist = os.listdir(path)
    for filename in filelist:
        fileabs = os.path.join(path,filename)
        if os.path.isdir(fileabs):
            print("目录： ",fileabs)
            zhan(fileabs)
        else:
            print("普通文件: ",fileabs)



zhan(r"C:\Users\Administrator\Desktop")














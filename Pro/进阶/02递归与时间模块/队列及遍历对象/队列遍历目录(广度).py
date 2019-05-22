import os
import collections


def get_alldirqe(path):
    que = collections.deque()
    #进队

    que.append(path)

    while len(que) != 0:
        #出队数据
        dirpath = que.popleft()
        #找出所有的文件
        filelist = os.listdir(dirpath)
        for filename in filelist:
            #绝对路径
            fileabs = os.path.join(dirpath,filename)
            #判断是否是目录，如果是就进队，不是就打印
            if os.path.isdir(fileabs):
                print("目录： ",filename)
                que.append(fileabs)
            else:
                print("文件： ",filename)


get_alldirqe(r"/Users/oukoto/Desktop")



















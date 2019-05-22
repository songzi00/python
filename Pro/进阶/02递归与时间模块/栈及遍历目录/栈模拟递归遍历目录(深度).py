import os

def get_alldirdeep(path):
    stack = []
    stack.append(path)
    #处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        # 取出栈里面的数据
        dirpath = stack.pop()
        filelist = os.listdir(dirpath)
        # 把目录遍历出来
        for filename in filelist:
            fileabs = os.path.join(path,filename)
            if os.path.isdir(fileabs):
                #如果是目录就压栈，否则打印普通文件
                print("目录： ",filename)
                stack.append(fileabs)
            else:
                print("普通文件： ",fileabs)


#         处理每一个文件，如果是普通文件就打印，如果是目录就将目录的地址压栈
get_alldirdeep(r"/Users/oukoto/Desktop/os")





































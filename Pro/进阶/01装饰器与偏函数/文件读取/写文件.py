import time

path = r"/Users/oukoto/Desktop/duoduo.txt"
f = open(path,"a")





# 写文件

#1、将信息写进缓冲区
f.write("songzi is nice women")

# 2、刷新缓冲区(直接把内部缓冲区的数据写进文件，而不是等待关闭自动刷新缓冲区）
f.flush()

# while 1:
#     f.write("songzi is nice women")
#     f.flush()
#     time.sleep(0.1)

with open(path,"a") as duoduo:
    duoduo.write("i miss you")































f.close()
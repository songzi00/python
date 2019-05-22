# import os
# import collections
# #把数据放进栈里面
# #当栈里面的数据不为0的时候
# # 把数据从栈里面取出来
# # 转换成列表的形式
# # 把列表的每一个数据循环出来
# #转换成绝对路径
# # 判断是否是目录，如果是目录，那么把它添加进path再次判断
#
# def alldir(path):
#     stack = []
#     stack.append(path)
#     while len(stack) != 0:
#         dick = stack.pop()
#         filelist = os.listdir(dick)
#         for filename in filelist:
#             abs = os.path.join(path,filename)
#             if os.path.isdir(abs):
#                 print("目录：",abs)
#             else:
#                 print("普通文件：",abs)
#
# alldir(r"/Users/oukoto/Desktop/os")
#
#
#
#
#
#
#
#
# # def allqe(path):
# #     que = collections.deque()
# #     que.append(path)
# #     while len(que) != 0:
# #         dick = que.popleft()
# #         list = os.listdir(dick)
# #         for name in list:
# #             abs = os.path.join(dick,name)
# #             if os.path.isdir(abs):
# #                 print("目录： ",abs)
# #                 que.append(abs)
# #             else:
# #                 print("普通文件： ",abs)
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
# # allqe(r"/Users/oukoto/Desktop/os")
#
#
#
#
#
import random






import random





# row = 3*2
# for i in range(1, row, 2):
#     space_count = (row-i)//2
#     print(' '*space_count,end="")
#     for j in range(i):
#         print('*', end="")
#     print()
#
# s = range(1,2,100)
# print(s)

row = 6*2
pos_line = [num for num in range(5) if num%2!=0]
# print(pos_line)
list = [1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     pos_line = [num for num in range(i)]
#     print(pos_line)
#     break
# liebiao = range(0, 10, 3)
for i in range(1,row,2):
    # print(row-i)
    # print((row-i)//2)
    space_count = (row-i)//2
    pos_line = [num for num in range(i) if num%2!=0]
    # print(i)
    print('空格'*space_count,end)






































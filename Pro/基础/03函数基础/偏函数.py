import functools






#偏函数：
def int2(str,base = 2):   #定义两个形参
    return int(str,base)  #把两个参数给int化
print(int2("1011"))

#把一个参数给固定，形成一个新的函数

int3 = functools.partial(int,base = 2)
print(int3("1111"))


int4 = functools.partial(int,base = 2)
print(int4("1110"))
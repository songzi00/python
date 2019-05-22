

"""
continue
作用：跳过当前循环中的剩余语句，然后继续下一次循环。
注意：continue只跳过离它最近的循环


"""

for i in range(20):
    if i % 2 != 0:
        continue
    print(i)
    print("*")
    print("$")
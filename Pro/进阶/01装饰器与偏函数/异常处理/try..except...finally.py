

"""
try..except..finally

格式：
try:
    语句t
except错误表示码 as e:
    语句1
except错误表示码 as e:
    语句2
    ...
except错误表示码 as e:
    语句n

finally:
    语句e


#作用：语句t无论有无错误，都将执行最后的语句f






"""

try:
    print(1/0)
except NameError:
    print("000")
finally:
    print("必须执行我")


















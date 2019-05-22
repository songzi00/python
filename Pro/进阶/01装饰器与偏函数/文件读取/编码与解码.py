




# 编码
path = r"/Users/oukoto/Desktop/f1.txt"

with open(path,"wb") as f1:
    str = "you are my lover"
    f1.write(str.encode("utf-8"))

with open(path,"rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newdata = data.decode("utf-8")
    print(newdata)
    print(type(newdata))












































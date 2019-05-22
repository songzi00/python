
import  pickle #数据持久性模块
path = r"duoduo.txt"
 

# list

mylist = [1,2,3,4,"songzi"]
f = open(path,"wb")

pickle.dump(mylist,f)


f.close()


# 读取
f1 = open(path,"rb")
templist = pickle.load(f1)
print(templist)
f1.close()


# tuple
mylist = (1,2,3,4,"songzi")
f = open(path,"wb")

pickle.dump(mylist,f)


f.close()


# 读取
f1 = open(path,"rb")
templist = pickle.load(f1)
print(templist)
f1.close()


























































#


#位置参数
def makeshirt(c,y):
    print("this is " + c + " and "+ y)
makeshirt("m","hello world")
makeshirt(c = "L",y = "hello python") #关键字参数





#默认参数
def ms(a = "L",b = "i love python"):
    print("this shirt is " + a + " and " + b)

ms(a = "m")
ms(a = "s",b = "hello world")



#默认参数
#例子1
def dc(name = "hunan",county = "china"):
    print(name + " is in " + county)

dc("dalian")
dc(county = "AUS")
dc("东京","日本")


# #大小写
# def m(first,last):
#     full = first + " " + last
#     return full.title()
#
# all = "wang qin,zhang yongshun,zhang duoduo"
# n5 = all.split(",")
#
# for i in n5:
#     n6 = i.split(" ")
#     print(m(n6[0],n6[1]))
#
#
#形参变成可选的
#例子1
def n7(first,last,middle = " "):
    if  middle:
        full = first + " " + middle + " " + last
    else:
        full = first + " " + last
    return full.title()
n8 = n7("song","zi")
print(n8)
#
#
# #例子2
# def n9(n1,n2 = 0,n3 = 0):
#     if n2 != 0:
#         print(max(n1,n2,n3))
#     else:
#         print(max(n1,n3))
#
# n9(10)
#
#
#
#
# # 返回字典
# def car(ping,type,m = ""):
#     all = {"品牌：":ping,"类型":type}
#     if m:
#         all["价格"] = m
#     return all
# print(car("路虎","SUV","200万"))
#
#
#
#
#
#
#
# #while循环
#
#
# #例子1
# def forname(fname,lname):
#     fullname = fname +  " "  + lname
#     return fullname
# while True:
#     print("请输入您的姓名")
#     print("按q即可退出")
#
#     firstname = input("firstname: ")
#     if firstname == "q":
#          break
#
#
#     lastname = input("lastname: ")
#     if lastname == "q":
#             break
#     n10 =  forname(firstname,lastname)
#     print("hello, "  + n10  + "!")

# def num(n1,n2):
#     all = n1 + n2
#     return all
#
# while True:   #循环条件:有输入值的时候
#     print("请输入两位数字：")
#     nun1 = int(input())  #设定实参为后台输入的数
#     if nun1  == 10:     #加入输入的数字是10，那么跳出循环
#         break
#     nun2 = int(input()) #设定同样的条件，当nun2等于10的时候跳出循环
#     if nun2  == 10:
#         break
#
#     print(num(nun1,nun2))#当nun1,nun2都不等于10的时候，return all的函数




#
# #例子2
# def city_country(ci,cy):
#     all = ci + " " + cy
#     return all.title()
#
# while True:
#     print("请输入城市名字")
#     print("输入停即可停止")
#
#     city = input("城市: ")
#     if city ==  "停":
#         break
#     country = input("国家: ")
#     if country == "停":
#         break
#     print(city_country(city,country))
#
#
# #例子3
# def make(name,z):
#     all = {"歌手：":name,"专辑：":z}
#     return all
# while True:
#    print("请输入歌手与专辑名")
#    print("输入stop即可停止")
#
#    geshou = input("歌手: ")
#    if geshou == "stop":
#        break
#
#    zh = input("专辑：")
#    if zh == "stop":
#        break
#
#    print(make(geshou,zh))
#
#
#
#
#
# #传递列表
# def full(names):
#     for name in names:
#         n1 = "hello, " + name + "!"
#         print(n1)
# fullname = ["songi","zhangyonghun","duoduo"]
# full(fullname)
#
#
#
# 在函数中修改列表
def p(un,com):

    while un[:]:
        curr = un.pop()#把未完成的设计从最后一位删减到curr里面
        print("this is " + curr)#把curr依次打印出来
        com.append(curr)#把未完成的设计添加进com里面
def show(com):
    print("the following models have been :")
    for coms in com:#把com遍历出来
        print(coms)
un = ["liuqian","hejiong","xiena"]
com = []

p(un,com)
show(com)


def show_mg(magic):
    for magics in magic:
        print(magics)
magic = ["zhang","yong","shun"]
show_mg(magic)



#传递任意数量的参数
# def pizza(*all):
#     print("客人点的配料有：")
#     for alls in all:
#         print("-" + alls)
# pizza("j","c","you","me")


def pizza(size,*el):
    print("this pizza is " + str(size))#先把size给表达出来
    for els in el:     #然后把剩下来的参数遍历出来
        print("-" + els)
pizza(18,"song","zi","ni","wo")







# def bulid(first,last,**in_fo):
#     pro = {}
#     pro["firstname"] = first
#     pro["lastname"] = last
#     for key ,value in in_fo.items():
#         pro[key] = value
#     return pro
# user = bulid("song","zi",age = 18,sex = "women")
#
# print(user)

def s(*all):
    print("需要添加的有：")
    for alls in all:
        print("-" + alls)
s("we","are","the","world")



def me(first,last,**els):
    all = {}
    all["firstname"] = first
    all["lastname"] = last
    for key,value in els.items():
        all[key] = value
        return all
user = me("wang","qin",age = 18,love = "L")

print(user)



# def make_album(name,zhuanji,num = ""):
#
#     if num:
#         all = {
#             "歌手： ":name,
#             "专辑：":zhuanji,
#             "歌曲": num
#         }
#     else:
#         all = {
#             "歌手： ":name,
#             "专辑：":zhuanji
#         }
#
#     return all
#
# print(make_album("周杰伦","千里之外"))




def get_users(name):
    for names in name: #把形参的数据遍历出来
        print("hello, " + names.title()) #把数据的第一个字母大写
all_users = ["songzi","wangqin","zhangyongshun"] #设定实参
get_users(all_users) #引用实参







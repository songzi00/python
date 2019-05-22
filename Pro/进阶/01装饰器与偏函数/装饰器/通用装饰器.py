

def outer(func):
    def inner(*args,**kwargs):
        # 添加修改的功能
        print("wo are the world")
        func(*args,*kwargs)
        return inner

@outer

def say(name,age):
    print("my name is %s,i am &d" %(name,age))


say("songzi",18)






























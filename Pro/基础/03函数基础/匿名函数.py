


"""
概念"匿名函数不使用def这样的语句定义函数，是使用lambda来创建匿名函数
特点：
    1，lambda只是一个表达式，函数体比def简单
    2，lambda的主体是一个表达式，而不是代码块，仅能在表达式中封装简单的逻辑
    3，lambda函数有自己的命名空间，且不能访问自有参数列表之外的或全局命名空间里面的参数
    4，虽然lambda是一个表达式，而且看起来只能写一行，与c、c++中的内联函数不同。


"""
# 格式：lambda 参数1，参数2：语句
sum = lambda n1,n2:n1 * n2
print(sum(20,56))























































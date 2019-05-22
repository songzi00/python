import turtle
"""
简单的绘图工具，

提供一个小海龟，可以理解为一个机器。只能听懂有限的命令，
注意：绘图窗口的起点在正中间，默认朝向右。
方法：
1，运动命令
    forward（）向前移动X长度
    backward（）向后移动X长度
    right()向左
    left（）向右
    goto（x,y移动到坐标为（x,y)的地方
    speed()笔画速度
2，笔画控制命令
    up（）笔画抬起，在移动的时候不会绘图
    down()笔画落下，移动时会绘图
    setheading()改变绘图的朝向
    pensize()笔画粗细
    pencolor()笔画颜色
    reset（）重置窗口，重置设置
    clear（）重置窗口，保留设置
    circle(r,e)绘制一个圆形，r为半径，e为次数
    begin_full()开始填充
    fullcolor()
    end_full()  结束填充
    
    
    
    
3，其他命令
    done（）程序继续执行
    undo()撤销上一次的动作
    hideturtle()隐藏海龟
    showturtle（）显示海龟
    



"""

#导入turtle库

#turtle.speed(15)
"""
turtle.forward(100)
turtle.right(45)
turtle.goto(34,99)



turtle.goto(-112,79)
"""
turtle.begin_fill()
turtle.fillcolor("pink")
turtle.circle(100,steps = 30)
turtle.end_fill()

turtle.done()


import win32con
import win32gui
import random
QQWin = win32gui.FindWindow("TXGuiFoundation","QQ")

# 参数1：控制的窗体
# 参数2：大致方位HWND_TOPMOST上方
# 参数3：位置X
# 参数4：位置Y
# 参数5：长度
# 参数6：宽度
# 在Windows终端执行此脚本 python + 空格 + 脚本地址按回车

while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(QQWin,win32con.HWND_TOPMOST,x,y,400,400,win32con.SWP_SHOWWINDOW)
import win32con
import win32gui
import random
QQWin = win32gui.FindWindow("TXGuiFoundation","QQ")


# 系统客户端
import  win32com.client
import time

songzi = win32com.client.Dispatch("SAPI.SPVOICE")
# duoduo.Speak("zhangyongshun is loser")

# while QQWin:
#     QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
#     win32gui.ShowWindow(QQWin,win32con.SW_SHOW)
#     time.sleep(2)
#     win32gui.ShowWindow(QQWin, win32con.SW_HIDE)
#     songzi.Speak("stop,you can not play QQ")


songzi.Speak("dont let me go,please")











































#进程模块
import win32process

#系统模块
import  win32con
import  win32gui
import  win32api
import  ctypes


PROCESS_ALL_ACCESS = (0x000F0000|0x00100000|0xFFF)

#找窗体
win = win32gui.FindWindow("MainWindow","植物大战僵尸中文版")
#根据窗体找到进程号
hid,pid = win32process.GetWindowThreadProcessId(win)
#以最高权限打开进程
p = win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
data = ctypes.c_long()
#加载内存模块
md = ctypes.windll.LoadLibrary("C:\\Windows\\system32\\kernel32.dll")
#读取内存
md.ReadProcessMemory(int(p),375039320,ctypes.byref(data),4,None)
print("data = ",data)

# 新值
newData = ctypes.c_long(10000)
# 修改
md.WriteProcessMemory(int(p),375039320,ctypes.byref(newData),4,None)



























































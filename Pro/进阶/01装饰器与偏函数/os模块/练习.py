import win32process
import win32gui
import win32con
import win32api
import ctypes

PROCESS_ALL_ACCESS = (0x000F0000|0x00100000|0xFFF)

zhi = win32gui.FindWindow("MainWindow","植物大战僵尸中文版")
hid,pid = win32process.GetWindowThreadProcessId(zhi)
p = win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
data = ctypes.c_long()
md = ctypes.windll.LoadLibrary("C:\\Windows\\system32\\kernel32.dll")
md.ReadProcessMemory(int(p),373343624,ctypes.byref(data),4,None)
print("data = ",data)

newdata = ctypes.c_long(5000)
md.WriteProcessMemory(int(p),373343624,ctypes.byref(newdata),4,None)
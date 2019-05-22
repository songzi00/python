import calendar



"""
日历模块






"""

# 使用



# 返回指定某年某月的日历
print(calendar.month(2019,3))

#返回指定年的日历
# print(calendar.calendar(2019))

#判断闰年，返回true，否则返回false
print(calendar.isleap(2019))

#返回某个月的weekday的第一天和这个月总共天数
print(calendar.monthrange(2019,3))

#返回某个月数以每一周为元素的列表
print(calendar.monthcalendar(2019,3))

























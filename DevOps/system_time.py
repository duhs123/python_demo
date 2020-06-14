#coding: utf-8
import time

time_str = time.strftime("日期：%Y-%m-%d", time.localtime())
print(time_str)

time_str = time.strftime("时间：%H:%M", time.localtime())
print(time_str)
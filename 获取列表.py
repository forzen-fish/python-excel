"""
1:获取大表名字列表√
2：获取小表名字位置√
3：比对大小表名字是否相同√
4：如果大表内有小表的名字，删除小表内的名字√

"""

import xlrd
from xlutils.copy import copy
import os

#获取大表名字,形成列表，并整理
#打开文件
dabiao = xlrd.open_workbook("经管（913）.xls")
sheet_dabiao = dabiao.sheets()[0]#实例化对象
namelist_1 = sheet_dabiao.col_values(3) #取姓名列表

#删除列表中第一个‘姓名’，与最后一个空，从而获得一个可以遍历的列表
del namelist_1[0]
del namelist_1[-1]
print(namelist_1)

#h获取小表
xiao_biao = xlrd.open_workbook("农林经济管理 123.xls")
fb = copy(xiao_biao)
sheet_xiaobiao = xiao_biao.sheets()[0]
name_list = []


#一班
for i in range(2,31):
    name = sheet_xiaobiao.row(i)[1].value
    if name in namelist_1:
        name_list.append([i,1])

#二班
for i in range(2,33):
    name = sheet_xiaobiao.row(i)[3].value
    if name in namelist_1:
        name_list.append([i,3])



#三班
for i in range(2,35):
    name = sheet_xiaobiao.row(i)[5].value
    if name in namelist_1:
        name_list.append([i,5])

print(name_list)
f = open("list.txt",'w')
f.write(str(name_list))
f.close()














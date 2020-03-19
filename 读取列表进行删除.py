import xlrd
from xlutils.copy import copy
import os

#读取列表
f = open("list.txt","r")
pos_list = f.read()
f.close()

#转换列表
pos_list = eval(pos_list)



#表格处理
xiao_biao = xlrd.open_workbook("农林经济管理 123.xls")
fb = copy(xiao_biao)
sheet = fb.get_sheet(0)

for i in range(0,len(pos_list)):
    sheet.write(pos_list[i][0],pos_list[i][1],'  ')
    sheet.write(pos_list[i][0], pos_list[i][1]-1, '  ')
    os.remove("农林经济管理 123.xls")  # 删除源文件
    fb.save("农林经济管理 123.xls")  # 保存拷贝文件



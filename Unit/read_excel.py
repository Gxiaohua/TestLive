# -*- coding:utf-8 -*-
# 作者：小花
# 时间：2023/9/28 14:42
# 读取excel文件
import openpyxl
from openpyxl import workbook
import xToolkit
import os
import xlrd
xlrd.Book.encoding = "utf-8"
# excel_path = '\Config\live_api.xls'

# base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),r"/Config/"))
# base_path = os.path.abspath(os.path.dirname(os.getcwd()))
# excel_path = '\Config\live_api.xls'
# excel_path = os.getcwd()
# base_path = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), r"/Config/"))
# print(base_path)

newpath = os.chdir('D:\ApiTestWork\API_LiveTest\Config')
# # print(newpath)
#
filename = "live_api.xls"

base_path = os.path.join(os.getcwd(),filename)
# print(file)
class ReadExcel:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = base_path
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
    #     加载excel文件
        self.data = xlrd.open_workbook(self.excel_path)
    #     工作表，sheet对象
        self.table = self.data.sheets()[index]
    #获取excel有效行数
    def get_lines(self):
        '''
        获取excel有效行数
        :return:
        '''
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return rows

    def get_clos(self):
        '''
        获取列数
        :return:
        '''
        clos = self.table.ncols
        if clos >= 1:
            return clos
        return clos

    def get_value_list(self):
        '''
        拿到excel中的数据，存到list中
        :return:
        '''
        #拿到第一行的标题
        header = self.table.row_values(0)
        #总行数：
        rows = self.get_lines()
        #总列数：
        clos = self.get_clos()
        result = []
        j = 1
        for i in range(rows - 1):#eg:rows一共6行，去掉标题就是5行数据
            s = {}
            #从第五行取相对应的value值
            values = self.table.row_values(j)
            for x in range(clos):
                s[header[x]] = values[x]
            result.append(s)
            j += 1
        return result


if __name__ == '__main__':
    ReadExcel = ReadExcel()
    print(ReadExcel.get_value_list())







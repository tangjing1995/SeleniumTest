# -*- coding: UTF-8 -*-
import time

import xlrd
from utlis.file.FileUtil import file_utils

class Read_exec(object):
    file_path = "config/data.xlsx"

    def __init__(self,file_name=None,index=0):
        self.data = xlrd.open_workbook(file_utils.location_file(self.file_path),encoding_override="utf-8")
        if file_name:
            self.table = self.data.sheet_by_name(file_name)
        else:
            self.table = self.data.sheet_by_index(index)

    def __get_lines(self):
        data =[]
        for i in range(self.table.nrows):
            data.append(self.table.row_values(i))
        return data

    def __get_columns(self):
        data =[]
        for i in range(self.table.ncols):
            data.append(self.table.col_values(i))
        return data

    def get_data(self):
        list =[]
        data = self.__get_lines()
        for i in range(len(data)):
            item = []
            for x in range(len(data[i])):
                if i>0 and x>0:
                    info = data[i][x]
                    if info!=None:
                        item.append(info)
            if item!=None and item!=[]:
                list.append(item)
        return list


read_exec = Read_exec()
if __name__ == '__main__':
    print (read_exec.get_data())

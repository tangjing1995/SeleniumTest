# -*- coding: UTF-8 -*-
import os
import sys
# from utlis.file.FileUtil import file_utils
# path = os.path.split(os.path.realpath(__file__))[0]  # 定位类目录
# print(path)
# sys.path.append(path)
# from case.Test_ddt_case import Test_ddt_case


if __name__ == '__main__':
    lists = [("1", "2", "3"), ("1", "2", "3")]
    # Test_ddt_case().run()
    for i in  range(len(lists)):
        print(lists[i][0])

    pass

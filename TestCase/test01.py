# -*- coding:utf-8 -*-
# 作者：小花
# 时间：2023/10/5 13:36
import sys
import os
path = os.getcwd()
sys.path.append(path)
from Unit.read_excel import ReadExcel
import pytest
import allure

case_data = ReadExcel().get_value_list()

@pytest.mark.parametrize('data',case_data)
def test1(data):
    print(data['url'])
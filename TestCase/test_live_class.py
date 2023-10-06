# -*- coding:utf-8 -*-
# 作者：小花
# 时间：2023/9/28 15:49
import json
import os

import pytest
import xToolkit
from Common.request_base import RequestBase
from Common.handle_assert import Assert
import allure
base_path = r'D:\ApiTestWork\API_LiveTest\Config\live_api.xls'
all_case = xToolkit.xfile.read(base_path).excel_to_dict()

@allure.epic('直播项目')
@allure.feature('课程管理')
class TestLiveClass:
    @allure.title('课程管理相关接口')
    @pytest.mark.parametrize('case',all_case)
    def test_add_course(self,case):
        url = case['url']
        get_method = case['请求方式']
        data = case['data'].encode('utf-8')
        get_header = eval(case['header'])
        code = case['预期状态码']
        key = 'wm-live-api'
        print(type(case),url,get_method,get_header,code)
        if get_method == 'post':
            res = RequestBase().send_post(url=url,data=data,key=key,cookie=None,header=get_header)
        else:
            res = RequestBase().send_get(url=url,params=data,key=key,cookie=None,header=get_header)
        test_assert = Assert()
        res = res.json()
        res_code = res['code']
        assert test_assert.assertCode(res_code, code)
        allure.dynamic.title(case['用例标题'])


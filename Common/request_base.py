# -*- coding:utf-8 -*-
# 作者：小花
# 时间：2023/9/27 23:06
import json

import requests
from json import dumps
from Common.logger import Logger
from Unit.read_int import ReadInt
from requests.packages.urllib3.exceptions import InsecureRequestWarning


# 禁用安全请求警告



requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logger = Logger().logger

class RequestBase(requests.Session):
    '''
    分装请求方法：
    1、判断是get、post请求：method
    2、传入路径：url
    3、参数：参数化 params
    '''
    #     # self.url = host + url1
    # def get_host(self,key=None,host=None,url=None):
    #     # 从config配置文件中获取域名
    #     if key == None:
    #         key = 'wm-live-api'
    #     if host == None:
    #         host = ReadInt().get_value(key)
    #         # host = 'http://baidu.com'
    #     if url == None:
    #         url = host
    #     else:
    #         url = host + url
    #     # print(url)
    #     return urldef

    def send_post(self,url,data,key=None,cookie=None,header=None):
        if key == None:
            url=url
        else:
            url=ReadInt().get_value(key)+url
        # print(url)
        # response = requests.post(url=url,data=data,cookies=cookie,headers=header)
        # return response
        '''
        get请求
        :param url: 请求地址
        :param data: 请求参数
        :param key: 
        :param cookie: 
        :param header: 
        :return: 
        '''
        try:
            res = self.request('post',url=url,data=data,cookies=cookie,headers=header,verify=False)
            # self.api_log('post',url=url,data=data,cookies=cookie,headers=header,code=res.status_code,res_text=res.content)
            return res
        except Exception as e:
            logger.error('接口请求异常,原因：{}'.format(e))
            raise e

    def send_get(self,url,params,key=None,cookie=None,header=None):
        if key == None:
            url=url
        else:
            url=ReadInt().get_value(key)+url
        # respose = requests.get(url=url,params=params,cookies=cookie,headers=header)
        # return respose
        try:
            res = self.request('get',url=url,params=params,cookies=cookie,headers=header,verify=False)
            # self.api_log('get', url=url, data=params, cookies=cookie, headers=header, code=res.status_code,res_text=res.content)
            return res
        except Exception as e:
            logger.error('接口请求异常,原因：{}'.format(e))
            raise e

    def api_log(self,method,url,data=None,json=None,cookies=None,headers=None,file=None,code=None,res_text=None,res_header=None):
        logger.info("请求方式====>{}".format(method))
        logger.info("请求地址====>{}".format(url))
        logger.info("请求头====>{}".format(dumps(headers,indent=4)))
        logger.info("请求参数====>{}".format(data))
        logger.info("请求体====>{}".format(dumps(json,indent=4)))
        logger.info("上传附件为======>{}".format(file))
        logger.info("Cookies====>{}".format(dumps(cookies,indent=4)))
        logger.info("接口响应状态码====>{}".format(code))
        logger.info("接口响应头为====>{}".format(res_header))
        logger.info("接口响应体为====>{}".format(res_text.decode("unicode_escape")))


    # def get_method(self,method,url=None,data=None,key=None,cookie=None,header=None):
    #     # if host == None:
    #     url = self.get_host()
    #
    #     if method == 'post':
    #         print('post')
    #         res = self.send_post(url,data,cookie,header)
    #     elif method == 'get':
    #         print('get')
    #         res = self.send_get(url,data,cookie,header)
    #
    #     try:
    #         res = json.loads(res)
    #     except:
    #         print('不是res ----------',res.text)
    #     print(res)
    #     return res
    # def run_main(self,method,url,data,cookie=None,get_cookie=None,header=None):
    #     # return get_value(url)
    #     #获取配置文件中内容
    #     # base_url = ReadInt.get_value('wm-live-api')
    #     # if 'http' not in url:
    #     #     url = base_url+url
    #     # print(url)
    #     # 执行方法，传递method、url、data参数
    #     if method == 'get':
    #         res = self.send_get(url,data,cookie,header)
    #     else:
    #         res = self.send_post(url,data,cookie,header)
    #     try:
    #         #请求成功，把结果json格式化
    #         res = json.loads(res)
    #     except:
    #         print('这个结果是一个text')
    #     return res


if __name__ == '__main__':
    RequestBase = RequestBase()
    # RequestBase.send_get('https://www.baidu.com','111')







# -*- coding:utf-8 -*-
# 作者：小花
# 时间：2023/9/27 21:44

#读取配置文件 - config文件中得内容
import configparser
import os
print(os.getcwd())
class ReadInt:
    def __init__(self,file_name=None,node=None):
        path = 'D:\ApiTestWork\API_LiveTest\Config\config.int'
        if file_name == None:
            self.file_name = path
        if node == None:
            self.node = 'WmLive'
        else:
            self.node = node
        self.cf = self.get_config(self.file_name)

    #获取配置文件
    def get_config(self,file_name):
        cf = configparser.ConfigParser()
        #读取配置文件路径
        cf.read(file_name,encoding='UTF-8')
        return cf

    #获取配置文件中的内容
    def get_value(self,key):
        value = self.cf.get(self.node,key)
        print(value)
        return value


ReadInt()
# ReadInt().get_value('wm-auth-api')
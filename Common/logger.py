# -*- coding:utf-8 -*-
# 作者：小花
# 时间：2023/10/3 15:14
'''
    第一步：导入logging
    第二步：创建日志记录器，使用logging模块中getlogger函数得到一个logger对象，logger函数后面加上需要记录日志的模块名称，
    通过setlever设置日志级别。
    第三步：添加处理器：通过logger.addHandler(headler_name),为logger对象添加一个处理器
    处理器有三种：StreamHeadler，HileHandler，NullHandler
        如：创建StreamHeadler
            sh = logging.streamHeadler()
            创建 StreamHandler 之后，可以通过使用以下方法设置日志级别，设置格式化器 Formatter，增加或删除过滤器 Filte
            ch.setLevel(logging.WARN) # 指定日志级别，低于WARN级别的日志将被忽略
            ch.setFormatter(formatter_name) # 设置一个格式化器formatter
            ch.addFilter(filter_name) # 增加一个过滤器，可以增加多个
            ch.removeFilter(filter_name) # 删除一个过滤器
    第四步：使用logger对象中的debug、info、warn、error、crit记录日志
'''
import logging
from logging import handlers
import os
# log_pash = os.path.abspath(os.path.join())
# filename="{}\\Logs\\all_log.log".format(log_path)
# filename = r'../Logs/all_log.log''
# class Logger:
filename = r'D:\ApiTestWork\API_LiveTest\Logs\all_log.log'
#     level_relations = {
#         'debug':logging.DEBUG,
#         'info':logging.INFO,
#         'warning':logging.WARN,
#         'error':logging.ERROR,
#         'crit':logging.CRITICAL
#
#     }
#     def __init__(self,filename=filename,level='info',when='D',backupCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d]-%(levelname)s:%(message)s'):
#         #创建logger对象
#         self.logger = logging.getLogger(filename)
#         # 设置日志等级
#         self.logger.setLevel(self.level_relations.get(level))
#         #添加处理器 - handler
#         # 往屏幕上输出
#         sh = logging.StreamHandler()
#         # 设置输出格式
#         format_str = logging.Formatter(fmt)
#         sh.setFormatter(format_str)
#         # 定时生成新日志文件  将日志文件写入filename，when指时间间隔的类型，interval为2天，backCount决定留几个日志文件
#         th = handlers.TimedRotatingFileHandler(filename=filename,when=when,interval=2,backupCount=backupCount,encoding='utf-8')
#         th.setFormatter(format_str)
#         # 为实例logger添加处理器
#         self.logger.addHandler(sh)
#         self.logger.addHandler(th)


class Logger:
    level_count={
        "debug":logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }
    def __init__(self,filename=filename,level='info',when='D',backupCount=3,fmt='%(asctime)s-%(pathname)s[line:%(lineno)d]-%(levelname)s:%(message)s'):
        self.logger =logging.getLogger(filename)
        # 设置日志等级
        self.logger.setLevel(self.level_count.get(level))
        # 处理一下格式
        format_str = logging.Formatter(fmt)
        # 创建处理器 - headers  控制台
        sh = logging.StreamHandler()
#         设置日志输出的格式
        sh.setFormatter(format_str)
#         创建定时更新日志
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,interval=2,backupCount=backupCount,encoding='utf-8')
        th.setFormatter(format_str)
#         实例对象中添加处理器
        self.logger.addHandler(sh)
        self.logger.addHandler(th)
#
# logger = Logger().logger
# logger.info('写入日志')








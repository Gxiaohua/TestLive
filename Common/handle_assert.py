# -*- coding:utf-8 -*-
# 作者：小花
# 时间：2023/10/3 21:27
import json
from json import dumps
from Common.logger import Logger
logger = Logger().logger
class Assert:
    '''
    断言是否等于
    :param actual: 实际值
    :param expected: 预期值
    :return:
    '''
    def assertEquals(self,actual,expected):
        try:
            assert str(actual) == str(expected)
            # logger.info('断言成功:实际值:{} 等于 预期值:{}'.format(actual,expected))
        except AssertionError as e:
            logger.error('断言失败:实际值:{} 不等于 预期值:{}'.format(actual,expected))
            #抛出异常
            raise AssertionError

    def assertTrue(self,actual):
        '''
        判断是否为真
        :param actual:实际值
        :return:
        '''
        try:
            assert actual == True
            # logger.info('断言成功，实际值:{} 为真'.format(actual))
        except AssertionError as e:
            logger.error('断言失败，实际值：{} 不为真'.format(actual))
            raise AssertionError

    def assertIn(self,content,target):
        '''
        断言是否包含
        :param content: 包含文本
        :param target: 目标文本
        :return:
        '''
        try:
            assert content in target
            # logger.info('断言成功，目标文本：{} 包含 文本：{}'.format(target,content))
        except AssertionError as e:
            logger.error('断言失败，目标文本：{} 不包含 文本：{}'.format(target,content))
            raise AssertionError

    def assertCode(self,code,expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            logger.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            logger.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            logger.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            logger.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            logger.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            raise

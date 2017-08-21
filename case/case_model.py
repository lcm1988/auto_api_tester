#coding:utf-8
import unittest
from json import loads
from urllib import urlencode
from conf import basedata
from tools.result_decorator import decorator
from tools.http_connector import httpconnector

class case_device(unittest.TestCase):
    #定义初始数据方法
    def setUp(self):
        self.commonpara= basedata.commonpara.copy()
        #定义请求头
        self.headers= basedata.nt_headers.copy()

    @decorator
    def test_iphone_restart1(self):
        '''程序后台唤起1'''
        para=self.commonpara.copy()
        para['flag']=2
        url='http://toffee.app.test.tvfanqie.com/iphone/common/online?%s'%urlencode(para)
        a,b=httpconnector().conn(url,'GET',header=self.headers)
        b=loads(b)
        expect_json={
            "error": 0,
            "msg": "ok",
            "data": {}
        }
        return expect_json,b

    @decorator
    def test_iphone_restart2(self):
        '''程序后台唤起2'''
        b=self.test_iphone_restart1(func_data=True)[1]
        expect_json={
            "error": 0,
            "msg": "ok",
            "data": {}
        }
        return expect_json,b

if __name__=="__main__":
    unittest.main()
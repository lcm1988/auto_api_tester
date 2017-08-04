#coding:utf-8
import unittest
from json import loads
from urllib import urlencode
from conf import basedata
from tools.result_decorator import decorator
from tools.http_connector import httpconnecter

class case_device(unittest.TestCase):
    #定义初始数据方法
    def setUp(self):
        self.commonpara= basedata.commonpara
        #定义请求头
        self.headers= basedata.nt_headers
    @decorator
    def test_iphone_restart(self):
        '''程序后台唤起'''
        para=self.commonpara
        para['flag']=2
        url='http://toffee.app.test.tvfanqie.com/iphone/common/online?%s'%urlencode(para)
        a,b=httpconnecter().conn(url,'GET',header=self.headers)
        b=loads(b)
        expect_json={
            "error": 0,
            "msg": "ok",
            "data": {}
        }
        return expect_json,b

if __name__=="__main__":
    unittest.main()
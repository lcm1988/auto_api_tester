#coding:utf-8
import httplib2
import urllib2
import gzip
import StringIO
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from conf.config import USE_PROXY,PROXY_HOST,PROXY_PORT

class httpconnecter():
    def __init__(self):
        pass

    #通过代理访问指定请求并返回请求结果
    def conn(self,url='',method='GET',para='',header={}):
        if USE_PROXY:
            h = httplib2.Http(proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, PROXY_HOST, int(PROXY_PORT)))
        else:
            h=httplib2.Http()
        if method.upper()=='GET':
                A,B=h.request(url,'GET',headers=header) if header else h.request(url,'GET')
        elif method.upper()=='POST':
            if para:
                A,B=h.request(url,'POST',para,header) if header else h.request(url,'POST',para)
            else:
                raise ValueError,'Para must be gaven when method is POST'
        return A,B

    #通过代理进行文件上传，并返回请求结果
    #para格式：{"arg1":"arg1","file1": open(r"F:\111.png", "rb")}
    def file_transer(self,url='',para={},header={}):
        if USE_PROXY:
            proxy_handler = urllib2.ProxyHandler({'http':'%s:%s'%(PROXY_HOST,str(PROXY_PORT))})
            opener = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(opener)
        else:
            null_proxy_handler = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(null_proxy_handler)
            urllib2.install_opener(opener)
        register_openers()
        a,b = multipart_encode(para)
        header['Content-Length']=b['Content-Length']
        header['Content-Type']=b['Content-Type']
        try:
            req = urllib2.Request(url,a,header)
            result=urllib2.urlopen(req)
            #判断是否压缩报文
            if result.info().get('Content-Encoding', "") == 'gzip':
                buf = StringIO.StringIO(result.read())
                res=gzip.GzipFile(fileobj=buf)
                res=res.read()
            else:
                res=result.read()
            return res
        except Exception as e:
            print e

if __name__=="__main__":
    head={
        'Accept': 'text/html',
        'Accept-Encoding': 'gzip',
        'Host': 'toffee.app.test.tvfanqie.com',
        'Connection': 'Keep-Alive',
        'User-Agent': '360 Video App/2.1.0 Android/5.1 QIHU'
    }

    para={
        'uidshow':11543,
        'crumb':'a9e591',
        'vr':'2.7.0',
        'fquc':	'bmFtZT0lRTklOTclQTglRTglODMlODElRTQlQjglODklRTklODMlOEUmc2lnbj1iYzQ0NzgxOTFkYmIxMzNhN2NiZDNiYTQzNzA2MzdiMXhpYW5rYW51Y3VpZD0yMDAwMDAzOTYxOSZsb2dpbl90aW1lPTE1MDA2MjI1NzcmdGh1bWI9MV90MDBkZjU1MWE1ODNhODdmNGU5Jm5pY2s=',
        'mid':'f8f377c765b2615e3449f647fe09ab3b'
    }
    from urllib3.filepost import encode_multipart_formdata
    from urllib3.fields import RequestField
    fields=[RequestField()]
    fields = [("thumb" , open("e:\\111.png",'rb').read(), 'application/vnd.ms-excel')]


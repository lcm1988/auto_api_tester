#coding:utf-8
import os,sys

thispath = os.path.abspath(os.path.dirname(sys.argv[0]))
basepath= thispath[:-4]

#basepath=r"E:\\pyscript\\NT_APITEST\\"#单元测试写死，非单元测试注释改行

commonpara={
    'ch':'',
    'ver':21000,
    'vr':'2.1.0',
    'mid':'7dfe7793b85a93f0d7893cb0419102e9',
    'uidshow':'',
    'longitude':'116.490285',
    'latitude':'39.982712',
    'province':'北京市',
    'city':'北京市'
}
nt_headers={
    'Accept': 'text/html',
    'Host': 'toffee.app.test.tvfanqie.com',
    'Connection': 'Keep-Alive',
    'User-Agent': '360 Video App/2.1.0 Android/5.1 QIHU'
}
msg_headers={
    'Accept': 'text/html',
    'Host': 'toffeemsg.app.test.tvfanqie.com',
    'Connection': 'Keep-Alive',
    'User-Agent': '360 Video App/2.1.0 Android/5.1 QIHU'
}
if __name__=="__main__":
    print basepath
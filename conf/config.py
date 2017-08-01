#coding:utf-8

#只对比结构,不care数据
CMP_FRAME_ONLY=True

#debug模式，为真时打印对比结果
IS_DEBUG=False

#case运行范围配置
RUN_ALL_CASE=True#该配置项为false时RUN_MODULES，RUN_CLASSES，RUN_CASES生效
RUN_MODULES=[]
RUN_CLASSES=[]
RUN_CASES=[]

#代理配置
USE_PROXY=True
PROXY_HOST='localhost'
PROXY_PORT=8888

#邮箱配置
RECIEVER_LIST= ['516315002@qq.com','*****@163.com']
SMTP_SERVER='smtp.163.com'
EMAIL_NAME='*****@163.com'
EMAIL_PWD='******'

#数据库配置


#缓存配置


#环境参数配置
#用户鉴权
PASSPORT_API={
    'SCHEME':['10.202.4.243','10.206.176.77'],
    'URI':'/getinfo/currentuser?clientIp=autotest&cookie=',
    'DOMAIN':'tuc.service.v.360.cn'
}

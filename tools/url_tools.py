#coding:utf-8
from json import dumps
from urllib import quote,unquote,urlencode

class urltools:
    def __init__(self):
        pass

    def url_unquote(self,quoted_str=''):
        if not isinstance(quoted_str,str):
            raise ValueError('错误的参数格式')
        try:
            para_list=[]
            if '&' in quoted_str:
                para_list=quoted_str.split('&')
            else:
                para_list.append(quoted_str)
            para_dict={}
            for i in para_list:
                tmp=i.split('=')
                para_dict[tmp[0]]=unquote(tmp[1])
            return dumps(para_dict,ensure_ascii=False)
        except:
            return False

    def url_quote(self,request_para={}):
        return urlencode(request_para)

if __name__=="__main__":
    print urltools().url_quote({'a':'中国','b':'music'})
    print  urltools().url_unquote('a=%E4%B8%AD%E5%9B%BD&b=music')

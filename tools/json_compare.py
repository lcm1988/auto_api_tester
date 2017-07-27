#coding:utf-8
from conf.config import IS_DEBUG

#数据对比，根据数据结构递归对比
class jsoncompare():
    def __init__(self,expect_data,real_data,is_debug=IS_DEBUG,debug_msg='##### COMPARE RESULTS #####'):
        self.expect_data=expect_data
        self.real_data=real_data
        self.data_compare_result=[]#数据对比结果
        self.frame_cmpare_result=[]#结构对比结果
        self.defaultroot=''
        self.compare(expect_data,real_data,self.defaultroot)
        if is_debug:
            print debug_msg
            for i in self.data_compare_result:print i
            for i in self.frame_cmpare_result:print i

    def compare(self,expect_data,real_data,path):
        try:
            if not isinstance(expect_data,(list,tuple,dict)):
                if isinstance(real_data,unicode):real_data=real_data.encode('utf-8')
                if not expect_data==real_data:
                    self.data_compare_result.append('%s:预期值:%s%s,实际值:%s%s'%(path,str(expect_data),type(expect_data),str(real_data),type(real_data)))
            elif isinstance(expect_data,(list,tuple)):#list,tuple
                if not isinstance(real_data,(list,tuple)):
                    #print type(real_data)
                    raise IndexError('实际数据不是list:%s'%path)#实际数据为非list/tuple类型
                for index,value in enumerate(expect_data):
                    try:
                        if index < len(real_data):
                            self.compare(value,real_data[index],'%s%s%d'%(path,'/下标:',index))
                        else:
                            raise IndexError('不存在的下标：%s%s%d'%(path,'/下标:',index))
                    except Exception,e:
                        if IndexError:
                            self.frame_cmpare_result.append('结构异常or数据缺失:%s'%e.message)
                        else:
                            self.frame_cmpare_result.append('未知异常:%s'%e.message)
            else:#dict
                if not isinstance(real_data,(dict)):
                    #print type(real_data)
                    raise IndexError('实际数据不是dict:%s'%path)#实际数据为非dict类型
                for key,value in expect_data.items():
                    try:
                        if key in real_data.keys():
                            self.compare(value,real_data[key],'%s%s%s'%(path,'/键:',str(key)))
                        else:
                            raise IndexError('不存在的键：%s%s%s'%(path,'/键:',key))
                    except Exception,e:
                        if IndexError:
                            self.frame_cmpare_result.append('结构异常or数据缺失:%s'%e.message)
                        else:
                            self.frame_cmpare_result.append('未知异常:%s'%e.message)
        except Exception,e:
            self.frame_cmpare_result.append('未知异常:%s'%e.message)



if __name__=="__main__":
    a={'a':[{"namelist":['a',1]},[1,2,3],{'age':3},{'age1':3},[1]]}
    b=[{"namelist":['b','2']},[1,'2'],[3],{'age12':3},{'age13':3}]
    res= jsoncompare(a,b)
    print '数据比对结果：'
    for i in res.data_compare_result:print i
    print '结构比对结果：'
    for i in res.frame_cmpare_result:print i








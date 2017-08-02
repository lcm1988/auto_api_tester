#coding:utf-8
import os,sys
import unittest
import HTMLTestRunner
import time

thispath = os.path.abspath(os.path.dirname(sys.argv[0]))
basepath = thispath[:-5]
sys.path.append(basepath)

from conf.config import RUN_ALL_CASE,RUN_MODULES,RUN_CLASSES,RUN_CASES

#获取run.py所在路径
path = os.path.abspath(os.path.dirname(sys.argv[0]))
#生成case文件所在路径
case_path= path.replace('main','case')

if RUN_ALL_CASE:
    #全局运行case
    #将case目录下的所有case生成suits
    suits=unittest.TestLoader().discover(case_path,pattern='case*.py')
else:
    #可控制case范围
    suit_list=[]
    files = os.listdir(case_path)
    #文件过滤
    if RUN_MODULES:
        modules_files= ["case."+i[:-3] for i in files if (i[:4]=="case" and i[-2:]=="py" and i in RUN_MODULES)]
    else:
        modules_files= ["case."+i[:-3] for i in files if (i[:4]=="case" and i[-2:]=="py")]
    for md in modules_files:
        moudle=__import__(md,fromlist=(md.split('.')[1],))
        cls_names=[cl for cl in dir(moudle) if cl[0:4]=="case"]
        for name in cls_names:
            classes=getattr(moudle,name)
            #suit=unittest.TestLoader().loadTestsFromTestCase(classes)#根据类直接生成suit
            #类过滤
            if RUN_CLASSES:
                if classes.__name__ not in RUN_CLASSES:continue
            #case过滤
            if RUN_CASES:
                case_names=[cn for cn in dir(classes) if (cn[0:4]=="test" and cn in RUN_CASES)]
            else:
                case_names=[cn for cn in dir(classes) if cn[0:4]=="test"]
            suit_list.append(unittest.TestSuite(map(classes, case_names)))
    suits= unittest.TestSuite(suit_list)

log_path=path.replace('main','log')
filename=log_path+r"\test_%d.html"%int(time.time())
fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'自动化测试报告desc',verbosity=2)
runner.run(suits)

#发送结果邮件，代码后续补充

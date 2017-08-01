#coding:utf-8
from conf.config import CMP_FRAME_ONLY
from tools.json_compare import jsoncompare

def decorator(fun):
    def test(*args):
        comment=fun.func_doc if fun.func_doc else fun.func_name
        print "%s RESULT OF \"%s\" %s"%("#"*10,comment,"#"*10)
        a,b= fun(*args)
        res=jsoncompare(a,b)
        if res.frame_cmpare_result or res.data_compare_result:
            assert len(res.frame_cmpare_result)==0
            if not CMP_FRAME_ONLY:
                assert len(res.data_compare_result)==0
        else:
            print '对比成功'
            pass
    return test


from wrapy.wrapfunc import Func,Wrap


def mylog_before( origin, wrapper ):
    of = wrapper
    print "--------<before>---------"
    print  of.args, of.kwargs, of.retval
    print "-------->before<---------"

def mylog_after( origin, wrapper ):
    print "--------<after>---------"
    print origin.origin_name,origin.args, origin.kwargs, origin.retval 
    print "-------->after<---------"

class MyApi(object):

    def work(self,*args):
        print "my api work something",args
        return "WORK"

    def wait(self,*args):
        print "my api waiting something",args
        return "WAIT"

    def done(self,*args ):
        print "my api done working",args 
        return "DONE"


api = MyApi()
wrap = Wrap()

api.done = wrap.after(   Func( target = api.done ) , Func(target = mylog_after ) )
api.wait = wrap.before( Func( target = api.wait ) ,  Func(target = mylog_before ) )
api.work = wrap.before_after( Func(target = mylog_before ),Func( target = api.work ) , 
                              Func(target = mylog_after ) )



api.work("get this work done")
api.wait("wait for me")
api.done("tasks done")

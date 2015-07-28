from wrapy import Wrapy
import time

def my_pre( *args, **kwargs ):
    print "my prefix function",args,kwargs
    return "pre return result"


def my_post( *args, **kwargs ):
    print "my postfix function",args,kwargs
 
    if "wrapy_pre_result" in kwargs:
        print "pre result   :-> ",kwargs['wrapy_pre_result']

    if "wrapy_ori_result" in kwargs:
        print "orig result  :-> ",kwargs['wrapy_ori_result'] 
    return "return post result"


def sleeping( ):
    print "sleeping"
    time.sleep(1)
    return "sleeping done"

def sleeping_s(s):
    print "sleeping s",s
    time.sleep(s)
    return "slept for ",s

def sleeping_st(s,t):
    print "sleeping s+t",s,t
    time.sleep(s+t)
    return "slept for t+s",s+t

def sleeping_time( atime = 1):
    print "sleeping_time",atime
    time.sleep( atime )
    return "slept for time atime"

def sleeping_a_time(a,atime = 1):
    print "sleeeeep"
    time.sleep( a+atime)
    return "slept for",a,atime
    

wrp = Wrapy()
# wrapy_ori_result = None, wrapy_pre_result=None
sleeping= wrp.prepost(sleeping,my_pre, my_post )
print sleeping( wrapy_ori_result=None, wrapy_pre_result=None)
sleeping_s = wrp.prepost(sleeping_s, my_pre, my_post )
print sleeping_s(1,wrapy_pre_result=None, wrapy_ori_result=None)
sleeping_st =  wrp.prepost(sleeping_st, my_pre, my_post )
print sleeping_st(1,1)
sleeping_time =  wrp.prepost(sleeping_time, my_pre, my_post )
print sleeping_time(atime = 1)
sleeping_a_time =  wrp.prepost(sleeping_a_time, my_pre, my_post )
print sleeping_a_time( 1, atime = 1)












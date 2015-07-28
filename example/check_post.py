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
    return "post result"


    
 
    return "my postfix result"

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

def sleeping_time( atime = 1):
    print "sleeping_time",atime
    time.sleep( atime )

def sleeping_a_time(a,atime = 1):
    print "sleeping_a_time",a,atime

wrp = Wrapy()

sleeping_s = wrp.prepost(sleeping_s,my_pre, my_post )
print sleeping_s( 3, wrapy_ori_result = None, wrapy_pre_result=None)

'''
sleeping_s = wrp.pref(sleeping_s, my_pref )
sleeping_s(1)
sleeping_st =  wrp.pref(sleeping_st, my_pref )
sleeping_st(1,1)
sleeping_time =  wrp.pref(sleeping_time, my_pref )
sleeping_time(atime = 1)
sleeping_a_time =  wrp.pref(sleeping_a_time, my_pref )
sleeping_a_time( "ok", atime = 1)
'''











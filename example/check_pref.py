from wrapy import Wrapy
import time

def my_pre( *args, **kwargs ):
    print "my preix function",args,kwargs
    return "my preix result"

def sleeping( ):
    print "sleeping"
    time.sleep(1)

def sleeping_s(s):
    print "sleeping s",s
    time.sleep(s)

def sleeping_st(s,t):
    print "sleeping s+t",s,t
    time.sleep(s+t)

def sleeping_time( atime = 1):
    print "sleeping_time",atime
    time.sleep( atime )

def sleeping_a_time(a,atime = 1):
    print "sleeping_a_time",a,atime

wrp = Wrapy()

sleeping = wrp.pre(sleeping, my_pre )
sleeping()
sleeping_s = wrp.pre(sleeping_s, my_pre )
sleeping_s(1)
sleeping_st =  wrp.pre(sleeping_st, my_pre )
sleeping_st(1,1)
sleeping_time =  wrp.pre(sleeping_time, my_pre )
sleeping_time(atime = 1)
sleeping_a_time =  wrp.pre(sleeping_a_time, my_pre )
sleeping_a_time( "ok", atime = 1)












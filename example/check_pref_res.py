from wrapy import Wrapy
import time

def my_pref( *args, **kwargs ):
    print "my prefix function",args,kwargs
    return "my prefix result"

def sleeping( wrapy_pref_result = None):
    print "sleeping"
    time.sleep(1)
    print wrapy_pref_result

def sleeping_s(s, wrapy_pref_result = None):
    print "sleeping s",s
    time.sleep(s)
    print wrapy_pref_result

def sleeping_st(s,t, wrapy_pref_result = None):
    print "sleeping s+t",s,t
    time.sleep(s+t)
    print wrapy_pref_result

def sleeping_time( atime = 1, wrapy_pref_result = None ):
    print "sleeping_time",atime
    time.sleep( atime )
    print wrapy_pref_result

def sleeping_a_time(a,atime = 1, wrapy_pref_result = None):
    print "sleeping_a_time",a,atime
    print wrapy_pref_result

wrp = Wrapy()

sleeping = wrp.pref(sleeping, my_pref )
sleeping( wrapy_pref_result = None)
sleeping_s = wrp.pref(sleeping_s, my_pref )
sleeping_s(1, wrapy_pref_result = None)
sleeping_st =  wrp.pref(sleeping_st, my_pref )
sleeping_st(1,1, wrapy_pref_result = None)
sleeping_time =  wrp.pref(sleeping_time, my_pref )
sleeping_time(atime = 1 , wrapy_pref_result = None)
sleeping_a_time =  wrp.pref(sleeping_a_time, my_pref )
sleeping_a_time( "ok", atime = 1, wrapy_pref_result = None )












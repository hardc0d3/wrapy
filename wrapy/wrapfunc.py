def target_to_default( target, default ):
    if target is None: return default
    else: return target 

def _setattr (o , key, value ):
    o.__setattr__ ( key,value )
    return True

def def_to_attr( o, key, target, default ):
    _setattr(o, key, target_to_default( target, default ) )
    return True

def kv_to_attr( o, init_kv, default_kv  ):
    if init_kv is None: return False
    if default_kv is None: return False

    for key,value in default_kv.items():
        if key in init_kv:
            print "key","value", key,init_kv[key] 
            o.__setattr__ ( key,init_kv[key] )
          
            #setattr(o,key,init_kv[key] )
        else:
            print "key","value", key,value
            o.__setattr__ ( key,value )
            setattr(o,key,value)
    return True

class DefaultA(tuple):
    def __new__(self):
        def _pass( *args, **kwargs ):
            pass
        #               f    args     kwargs  async origin
        return ( _pass, tuple(), dict(), None, None )

class DefaultKWA(dict):
    """ defaults kwargs for Func init """
    def __new__(self):
        def _pass( *args, **kwargs ):
            pass
        return dict(
        { 
          "target":_pass
         ,"args":tuple()
         ,"kwargs":dict()
         ,"async":None
         ,"origin":None
        })
     

class Func(object):
    """
    contains function data
    kwargs:

    target = target functino
    args   = args
    kwargs = kwargs
    async  = async object
    origin = Func object holding orginal function data when decorating

    init_args =  args ini list exact 4 args: ( target, args, kwargs, async, origin )
    init_kwargs = kw init dict any argument set or no key arg
    e.g { 'target':my_function } 
    """

    def __init__(self, target = None, args = None, kwargs = None, async = None,  origin=None,
                       init_args = None, init_kwargs = None ):
   
        #1st inti_args 
        self.retval = None
        self.origin = None

        if init_args is not None and len(init_args) == 5:
            if _setattr(self,'target',init_args[0]):
                if _setattr(self,'args',init_args[1]):
                    if _setattr(self,'kwargs',init_args[2]):
                        if _setattr(self,'async',init_args[3]):
                            if _setattr(self,'origin',inti_args[4]):
                                return True  
         
        default_kwa = DefaultKWA();    
        #2nd init_kvargs
        if kv_to_attr( self, init_kwargs, default_kwa ): return 
        
        #3th one by one
        
        if not def_to_attr( self,'target', target, default_kwa[ 'target' ] ):
            raise Exception('init failed') 
        if not def_to_attr( self,'args', args, default_kwa[ 'args' ] ):
            raise exception('init failed')
        if not def_to_attr( self,'kwargs', kwargs, default_kwa[ 'kwargs' ] ):
            raise Exception('init failed')
        if not def_to_attr( self,'async' ,async, default_kwa[ 'async' ] ):
            raise Exception('init failed')
        if not def_to_attr( self,'origin' ,async, default_kwa[ 'origin' ] ):
            raise Exception('init failed')
       
        # fix this mes 
        self.origin_name = self.target.__name__
        #print "DEBUG",self.origin_name
    def call(self):
        self.ret =  self.target(*self.args,**self.kwargs)
        return self.ret
        

    def call_wrapper(self):
        self.ret =  self.target( self.origin, self)
        return self.ret


class Wrap(object):
    def _wrap_after (self, origin, after):
        def wrap( func ):
            def wrapped(*args, **kwargs):
                 origin.args = args
                 origin.kwargs = kwargs
                 origin.retval = func(*args,**kwargs)
                 after.origin = origin
                 return after.call_wrapper()
            return wrapped
        return wrap

    def _wrap_before (self, origin, before):
        def wrap( func ):
            def wrapped(*args, **kwargs):
                 before.call_wrapper()
                 origin.retval = func(*args,**kwargs)
                 return origin.retval 
            return wrapped
        return wrap

    def _wrap_before_after(self,before,origin,after):
        def wrap( func ):
            def wrapped(*args, **kwargs):
                 before.call_wrapper()
                 origin.args = args
                 origin.kwargs = kwargs
                 origin.retval = func(*args,**kwargs)
                 after.origin = origin 
                 return after.call_wrapper()
            return wrapped
        return wrap

    
    def after(self, origin, after ):
        after.origin = origin
        origin.target = self._wrap_after( origin, after )( origin.target )
        return origin.target

    def before(self,origin, before ):
        before.origin = origin
        origin.target = self._wrap_before( origin, before )( origin.target )
        return origin.target
 
    def before_after(self, before, origin, after  ):
        #before.origin = origin
        after.orign = origin
        origin.target = self._wrap_before_after( before, origin, after )( origin.target )
        return origin.target

# prototypes for callbacks

def origin_callback( *args, **kwargs ):
    pass

# ortin,wrapper are Func objects
def wrapper_calback( orign, wrapper ):
    pass


class Wrapy(object):

    def __init__( self, pre_result_key = 'wrapy_pre_result',
                  ori_result_key = 'wrapy_ori_result' ):

        self._pre_result_key = pre_result_key
        self._ori_result_key = ori_result_key
# ----------------------------------------------------------------------------

    def pre( self, ori, pre ):
        """ pre injects function pre before ori(in(al) function """
        def f( *args, **kwargs ): 
            if args:
                if kwargs:  
                    if self._pre_result_key in kwargs:
                        kwargs[ self._pre_result_key ] = pre ( *args, **kwargs )
                        return ori( *args, **kwargs )
                    else:
                        pre( *args, **kwargs )
                        return ori( *args, **kwargs )
                else:
                    pre( *args )
                    return ori ( *args)
            else:
                if kwargs:
                    if self._pre_result_key in kwargs: 
                        kwargs[ self._pre_result_key ] = pre ( **kwargs )
                        return ori( **kwargs )
                    else:
                        pre( **kwargs ) 
                        return ori( **kwargs )
                else:
                    pre( ) 
                    return ori( )
        return f

# -----------------------------------------------------------------------------
    def post( self, ori, post ):
        """ post injects function post after function ori(inal) """
        def f( *args, **kwargs ):
            if args:
                if kwargs:
                    if self._ori_result_key in kwargs:
                        kwargs[ self._ori_result_key ] = ori ( *args, **kwargs )
                        return post( *args, **kwargs )
                    else:
                        ori( *args, **kwargs )
                        return post( *args, **kwargs )
                else:
                    ori( *args )
                    return post ( *args)
            else:
                if kwargs:
                    if self._ori_result_key in kwargs:
                        okwargs = dict(kwargs)
                        del okwargs[self._ori_result_key]
                        kwargs[ self._ori_result_key ] = ori ( **okwargs )
                        return post( **kwargs )
                    else:
                        ori( **kwargs )   
                        return post( **kwargs )
                else:
                    ori( )
                    return post( )
        return f





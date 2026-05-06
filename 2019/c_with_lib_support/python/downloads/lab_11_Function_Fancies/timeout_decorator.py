#! /usr/bin/env python
"""Sooo optional, advanced and esteric!
A TimeOut decorator with a variable argument in the
sugar requires nested decorators! """

import signal, time 

def MakeStrArgs(*args, **kwargs):
    all_args = ', '.join([str(a) for a in args] 
                        + ["%s=%s" % (k,v)
                            for (k, v) in kwargs.items()])
    return all_args
                
def TimeOut(timeout):
    """@TimeOut(3) before any function will cause it to
    time out in 3 seconds.  Then, when you call it, there
    will be a "RuntimeError" if it times out.
    """
    def DecoratorWrapper(Func):
        def WrappedFunction(*args, **kwargs):
            def AlarmHandler(signum, frame):
                report =  "%s(%s) timed out at %d seconds." % (
                    Func.__name__, MakeStrArgs(*args, **kwargs),
                    timeout)
                raise RuntimeError, report
            old = signal.signal(signal.SIGALRM, AlarmHandler)
            signal.alarm(timeout)
            try:
                result = Func(*args, **kwargs)
            finally:
                signal.signal(signal.SIGALRM, old)
                signal.alarm(0)
            return result
        return WrappedFunction
    return DecoratorWrapper

@TimeOut(2)
def TestArgs(*args, **kwargs):
    try:                        
        time.sleep(3)           
    except RuntimeError, info:  
        print info

def main():
    TestArgs(1, "one", {"one":1}, one=1)
    
if __name__ == '__main__':  
    main()
"""
$ timeout_decorator.py
TestArgs(1, one, {'one': 1}, one=1) timed out at 2 seconds.
$ """ 

import foo

def foo():
    #x = { "fld1": "eval" }
    #x.fld2 = "eval"
    return 0

def bar():
    if(1 == 2):
        return 0
    if(1+2 == 1+2):
        return 1
    if(1+2 == 1+2):
        foo()
    if(x == x):
        foo()
    

def funcs():
    foo(1)
    foo(1, 2)
    foo(1, 2, 3)


def cond():
    if True:
        bar()
    return False

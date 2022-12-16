# prog 19
# wap to get the count of local variables in the func

def var_count():
    x = 10
    y = 12.45
    z = 'python'
    a = 2 + 2j
    b = True
    # method 1:- finding local variables by using dir() function

    return len(dir())


print(var_count())
# method 2 : - using co_nlocals
print(var_count.__code__.co_nlocals)


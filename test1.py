from _functools import reduce
def Result(x,y):
    return x if (x>y) else y
I = [100,90,80,200]
ret= reduce(Result,I)
print(ret)

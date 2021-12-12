import math


def Skrug(S):
    """Returns the area of the circle by radius"""
    S = S**2 * math.pi
    return S
def min3(c, o, h):
    """Will find the minimum of three numbers"""
    if o >= c <= h:
        return c
    elif c >= o <= h:
        return o
    else:
        return h
def add(x, y):
    return x + y
def cub(x):
    return x*x*x
def hello_world():  
    print("hello world") 
def con(p, t, r):  
    return(p*t*r) / 100
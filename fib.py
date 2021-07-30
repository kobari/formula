import sys


def Fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)


def fibnormal(n):
    f = 1 #1
    x1 = 1 #1
    for i in range(2, n): #3*n
        x2 = x1
        x1 = f
        f = x1 + x2
    return f


if __name__=='__main__':
    sys.setrecursionlimit(9000)
    #print(Fib(8181))
    print(fibnormal(10))
    print(fibnormal(50))
    print(fibnormal(100))
    print(fibnormal(8181))

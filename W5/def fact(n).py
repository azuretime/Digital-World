def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n  


def factorial(n):
    a=1
    for i in range(1,n+1):
        a *= i
    return a




def fact(n):
    if n == 0:
        return 1
    else:
        num = 1
        while n >= 1:
            num = num * n
            n = n - 1
        return num
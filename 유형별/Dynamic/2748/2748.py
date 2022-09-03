def fib(n):
    if n ==0:
        return 0
    elif n==1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# print(fib(17))



def fib2(n):
    v0,v1 = 0,1
    for _ in range(n):
        v0,v1 = v1 , v1+v0
    return v0

n=int(input())
print(fib2(n))

n=int(input())
def fib1(n):
    if n==1 or n==2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


f=[0]*(n)

def fib2(n):
    if n<=1:
        return f[0]
    f[0],f[1]=0,1
    for a in range(2,n):
        f[a]=f[a-2]+f[a-1]
    return len(f)-2



print(fib1(n),fib2(n))


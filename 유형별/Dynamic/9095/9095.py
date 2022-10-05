n= int(input())

def fib(n):
    if n ==1 :
        return 1
    elif n ==2:
        return 2
    elif n==3:
        return 4
    else:
        return fib(n-1)+fib(n-2)+ fib(n-3)



for _ in range(n):
    a = int(input())
    print(fib(a))
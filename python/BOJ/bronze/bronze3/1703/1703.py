while 1:
    lst = list(map(int, input().split()))
    if lst[0]==0:
        break
    n = 1
    for a in range(lst[0]):
        kt=lst[2*a+1]
        lt=lst[2*a+2]
        n=n*kt-lt
    print(n)
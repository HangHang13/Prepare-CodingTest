

n=int(input())


for _ in range(n):
    lst= list(input())
    ant1=0

    for i in lst:
        if i=="(":
            ant1+=1
        else:
            ant1-=1
        if ant1<0:
            print("NO")
            break



    if ant1>0:
        print("NO")
    elif ant1==0:
        print("YES")
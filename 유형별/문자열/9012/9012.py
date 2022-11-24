

n=int(input())


for _ in range(n):
    lst= list(input())
    ant1=0
    ant2=0
    for i in lst:
        if i=="(":
            ant1+=1
        else:
            ant2+=1


    if ant1!=ant2:
        print("NO")
    else:
        print("YES")
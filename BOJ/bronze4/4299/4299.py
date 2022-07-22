a,b =map(int, input().split())
#a는 합 b는 차
ds=[]
ds.append(a)
ds.append(b)

c=abs(a-b)
d=c-min(ds)

ks=[]
ks.append(c)
ks.append(d)

if c+d ==a and c-d ==b:
    for a in ks:
        print(a, end=" ")
else:
    print(-1)


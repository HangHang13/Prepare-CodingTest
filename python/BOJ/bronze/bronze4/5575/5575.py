
i=0
while i<3:
    a,b,c,d,e,f = map(int, input().split())
    a1=0
    a1+=a*60*60+b*60+c
    b1=0
    b1+=d*60*60+e*60+f
    k=b1-a1
    h=0
    m=0
    s=0
    h=k//3600
    m=(k%3600)//60
    s=(k%3600)%60

    print(h,m,s)
    i+=1
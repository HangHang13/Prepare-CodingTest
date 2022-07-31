a,b,c,d = map(int, input().split())
e,f,g,h = map(int, input().split())

aa=0
bb=0
aa+=a+b+c+d
bb+=e+f+g+h

if aa>bb:
    print(aa)
elif aa<bb:
    print(bb)
else:
    print(aa)
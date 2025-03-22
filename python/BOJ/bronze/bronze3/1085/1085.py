a,b,c,d = map(int, input().split())


e,f = 0,0

ac = abs(a-c)
bd = abs(b-d)
ae = abs(a-e)
bf = abs(b-f)

print(min(ac,bd,ae,bf))
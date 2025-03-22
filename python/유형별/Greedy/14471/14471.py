n,m = map(int,input().split())


card=[]
ans=0
cos=0

for _ in range(m):
    a,b = (map(int,input().split()))
    if a<n:
        card.append((a,b))
    else:
        ans+=1

card.sort(reverse=True)


if (m-1) == ans:
    print(0)
else:
    for lst in range(m-1-ans):
        cos+= (n-card[lst][0])
    print(cos)
n= int(input())

res =0
ans= 0

for a in range(1,n+1):
    res+=a
    ans+=1
    if res>n:
        ans-=1
        break
print(ans)
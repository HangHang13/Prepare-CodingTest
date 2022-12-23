n,k = map(int, input().split())

cnt=0
while k:

    if k%2==0:
        k=k//2
    else:
        k-=1
        cnt+=1
    if k == n:
        break

print(cnt)
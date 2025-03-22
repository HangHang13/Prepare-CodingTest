


n,l  = map(int, input().split())


p=0
cnt=0
for _ in range(n):
    a,b,c = map(int,input().split())
    cnt += a-p
    p=a
    if cnt%(b+c) <= b:
        cnt += (b-(cnt%(b+c)))


cnt+=(l-p)
print(cnt)

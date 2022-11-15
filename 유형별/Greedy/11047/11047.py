n,k=map(int, input().split())


lst=[]
for _ in range(n):
    lst.append(int(input()))


lst.sort(reverse=True
)

cnt=0
for num in lst:
    if k>=num:
        cnt+=k//num
        k%=num
        if k<=0:
            break

print(cnt)
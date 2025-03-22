n=int(input())

lst = list(map(int, input().split()))

cnt=0
net=0
for i in lst:
    if i == net:
        cnt+=1
        net+=1
        if net>2:
            net=0
    else:
        continue

print(cnt)

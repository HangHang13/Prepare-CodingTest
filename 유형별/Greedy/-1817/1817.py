
n,m = map(int, input().split())
if n != 0:
    lst = list(map(int, input().split()))   
cnt= 1
buffer = 0

if n != 0:
    for i in range(0, len(lst)):
        if buffer + lst[i] <=m:
            buffer += lst[i]
        else:
            cnt+=1
            buffer = lst[i]
else:
    cnt = 0


print(cnt)
    

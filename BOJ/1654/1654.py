
k,n = map(int, input().split())
a=[]
for _ in range(k):
    a.append(int(input()))

start =1
end = max(a)

while start<=end:
    mid = (start+end)//2
    cnt=0
    for i in a:
        cnt+=i//mid
    if cnt>= n:
        start =mid+1
    else:
        end=mid-1

print(end)
print(11//2)
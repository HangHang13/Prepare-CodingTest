import sys
input=sys.stdin.readline
n=int(input())

lst = [[0]*2 for _ in range(n)]

for z in range(n):
    a,b = map(int, input().split())
    lst[z][0] = a
    lst[z][1] = b


lst.sort(key=lambda x:(x[1],x[0]))

cnt=1
end_ = lst[0][1]

for i in range(1,n):
    if lst[i][0] >= end_:
        cnt+=1
        end_ = lst[i][1]

print(cnt)

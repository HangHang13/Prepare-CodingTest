import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int, input().split())

arr=[]

for a in range(m):
    arr.append(list(map(int, input().split())))

q=deque()
for y in range(m):
    for x in range(n):
        if arr[y][x] ==1:
            q.append((y,x))

dy=[1,-1,0,0]
dx=[0,0,1,-1]
ans=0

#bfs 로 배열에 1씩 더해준다. 가장 큰 값 출력하면 됨
while q:
    y,x = q.popleft()

    for k in range(4):
        ny=y+dy[k]
        nx=x+dx[k]
        if ny>=0 and ny<m and nx>=0 and nx<n:
            if arr[ny][nx]==0:
                arr[ny][nx] = arr[y][x]+1
                q.append((ny,nx))
            else:
                continue
        else:
            continue

# 만약 0이 있으면, 즉 토마토가 다익지 않았다면 -1 출력, 중단 exit
for a in arr:
    for b in a:
        if b==0:
            print(-1)
            exit(0)
    ans = max(ans,max(a))


print(ans-1)






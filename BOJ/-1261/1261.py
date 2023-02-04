from collections import deque


n, m = map(int, input().split())

arr = []

for _ in range(m):
    arr.append(input())

dist = [[-1]*n for _ in range(m)]
dist[0][0] =0
q =deque()
dx=[0,0,-1,1]
dy=[1,-1,0,0]
q.append((0,0))

while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<m and 0<=nx<n:
            if dist[ny][nx] ==-1:
                if arr[ny][nx]=='0':
                    q.appendleft((ny,nx))
                    dist[ny][nx] = dist[y][x]
                elif arr[ny][nx] =='1':
                    q.append((ny,nx))
                    dist[ny][nx] = dist[y][x]+1
print(dist[m-1][n-1])
print(dist)

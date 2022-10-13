import collections

dy= [1,-1,0,0]
dx=[0,0,-1,1]

q=collections.deque([])

n,m = map(int,input().split())



arr = [list(map(int, input())) for _ in range(n)]
vis= [[0]*m for _ in range(n)]
q.append((0,0))

while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<m and arr[ny][nx] ==1 and vis[ny][nx] ==0:
            q.append((ny,nx))
            arr[ny][nx] = 2
            vis[ny][nx] = vis[y][x] +1


print(vis[n-1][m-1]+1)


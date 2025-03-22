t = int(input())
import sys
sys.setrecursionlimit(10000)
import collections
def bfs(y,x):
    q= collections.deque()
    q.append((y,x))
    vis[y][x] =True

    while q:
        y,x = q.popleft()
        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=nx<m and 0<=ny<n:
                if arr[ny][nx] ==1 and not vis[ny][nx]:
                    vis[ny][nx] = True
                    q.append((ny, nx))
def dfs(y,x):
    if y<0 or x<0 or y>=n or x>=m or arr[y][x] != 1:
        return

    arr[y][x]=0
    dfs(y+1,x)
    dfs(y-1,x)
    dfs(y,x-1)
    dfs(y,x+1)




dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(t):
    m,n,k = map(int,input().split())


    arr = [[0] *m for _ in range(n)]
    vis = [[False] * m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())

        arr[y][x] = 1
    cnt=0
    for y in range(n):
        for x in range(m):
            if arr[y][x] ==1:
                dfs(y,x)
                cnt+=1



    print(cnt)
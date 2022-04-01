import sys
import collections
sys.stdin = open('input.txt')

dy=[1,-1,0,0]
dx=[0,0,1,-1]
def bfs(y,x):
    q=collections.deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or ny>=n or nx<0 or nx>=m:
                continue
            if arr[ny][nx]==0 and arr[y][x]==1:
                vis[y][x] =1
                #q.append((ny,nx))





n , m = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
vis= [[0]*m for _ in range(n)]
ao=[]
ko=[]

for y in range(n):
    for x in range(m):
        if arr[y][x] !=0:
            ao.append((y,x))

bfs(0,0)
for y, x in ao:
    bfs(y,x)

for a in vis:
    for b in a:
        print(b, end=" ")
    print()
print()
for a in arr:
    for b in a:
        print(b, end=" ")
    print()
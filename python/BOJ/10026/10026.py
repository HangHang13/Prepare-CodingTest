import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')

n = int(input())

dy= [0,0,-1,1]
dx= [1,-1,0,0]

arr=[]
for _ in range(n):
    arr.append(list(input().strip()))


vis = [[False] * n for _ in range(n)]


def dfs(y,x):

    vis[y][x] = True
    color = arr[y][x]
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<n:
            if vis[ny][nx] == False:
                if arr[ny][nx] == color:
                    dfs(ny,nx)

cnt1=0
for y in range(n):
    for x in range(n):
        if vis[y][x] == False:
            dfs(y,x)
            cnt1+=1

cnt2=0
#적록색약
for y in range(n):
    for x in range(n):
        if arr[y][x] == 'R':
            arr[y][x] = 'G'

vis = [[False]* n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if vis[y][x] == False:
            dfs(y,x)
            cnt2+=1

print(cnt1,cnt2)


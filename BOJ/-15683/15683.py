n,m = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

vis = [[0] *m for _ in range(n)]
xy=[]
print(vis)
for y in range(n):
    for x in range(m):
        if arr[y][x] !=0:
            xy.append((y,x,arr[y][x]))


dy=[0,0,1,-1]
dx=[1,-1,0,0]

def count(vis):
    global cnt
    cnt=0
    for y in range(n):
        for x in range(m):
            if vis[y][x] ==0:
                cnt+=1
    return cnt

while xy:
    y,x,q = xy.pop(0)
    if q == 1:
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]


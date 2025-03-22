import sys
import collections
import copy
sys.stdin = open('input.txt')



n,m,fuel = map(int, input().split())

arr= []

for _ in range(n):
    data = (list(map(int, input().split())))
    grp = []
    for a in data:
        if a==1:
            grp.append(-1)
        else:
            grp.append(-2)
    arr.append(grp)

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
sy ,sx = map(int, input().split())
sy-=1
sx-=1
cos=[]

for _ in range(m):
    y,x, gy,gx = map(int, input().split())
    cos.append((y,x,gy,gx))

def cal(grp ,sy,sx):
    g= copy.deepcopy(grp)
    vis = [[False] * n for _ in range(n)]
    q=collections.deque()
    q.append((sy,sx))
    g[sy][sx]=0
    vis[sy][sx]=True
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0>nx or 0>ny or ny>=n or nx>=n :
                continue
            if g[ny][nx]==-1 or vis[ny][nx]==True:
                continue
            g[ny][nx] = g[y][x]+1
            vis[ny][nx]=True
            q.append((ny,nx))
    return g


print(cal(arr,sy,sx))

while True:
    if fuel <0:
        break
    if len(cos) ==0:
        break
    move = []
    gg = cal(grp,sy,sx)

    for h in cos:
        a,b,c,d= h
        dis = gg[a-1][b-1]
        if dis<0:
            continue
        move.append([dis,a-1,b-1,c-1,d-1])
    if len(move)==0:
        k=-1
        break
    else:
        move.sort(key=lambda x:(x[0],x[1],x[2]))
        if move[0][0]:pass
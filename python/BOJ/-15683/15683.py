n,m = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))


xy=[]

for a in arr:
    for b in a:
        print(b, end=" ")
    print()
print()
for y in range(n):
    for x in range(m):
        if arr[y][x] !=0:
            xy.append((y,x,arr[y][x]))

oney=[0,0]
onex=[1,-1]

twoy=[]

fivey=[0,0,1,-1]
fivex=[1,-1,0,0]

def count(vis):
    global cnt
    cnt=0
    for y in range(n):
        for x in range(m):
            if vis[y][x] ==0:
                cnt+=1
    return cnt

dy=[1,-1,0,0]
dx=[0,0,1,-1]
stack=[]
#xy는 큐
while xy:
    y,x,q = xy.pop(0)
    vis = [[0] * m for _ in range(n)]
    if q == 1:
        stack.append((y,x))
        while stack:
            for k in range(4):
                ny = y+dy[k]
                nx = x+dx[k]
                if 0<=ny<n and 0<=nx<m and arr[ny][nx] ==0 and vis[ny][nx] ==0:
                    vis[ny][nx] = 1
                    stack.append((ny,nx))
                    for a in vis:
                        for b in a:
                            print(b, end=" ")
                        print()
                    print()



import collections

dy=[1,-1,0,0]
dx=[0,0,1,-1]

n,k = map(int, input().split())
arr=[]
vir=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

for y in range(n):
    for x in range(n):
        if arr[y][x] !=0:
            vir.append((arr[y][x],y,x))

#시간 y좌표 x좌표
s,y,x =map(int, input().split())
vir.sort()
def bfs(s):
    q= collections.deque(vir)
    t=0
    while q :
        if t==s:
            break
        for _ in range(len(q)):
            z,y,x = q.popleft()
            for i in range(4):
                ny=y+dy[i]
                nx=x+dx[i]
                if 0<=ny<n and 0<=nx<n:
                    if arr[ny][nx] ==0:
                        arr[ny][nx]=z
                        q.append((arr[ny][nx], ny,nx))
        t += 1

bfs(s)
print(arr[y-1][x-1])

import collections

m,n,h =map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q= collections.deque()

#시작 좌표찾기


#3차원 이동
dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]


for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x]==1:
                q.append((z,y,x))

day= 0

while q :
    cnt = len(q)

    day+=1
    for _ in range(cnt):
        z, y, x = q.popleft()
        for k in range(6):
            nz = dz[k]+z
            ny = dy[k]+y
            nx = dx[k]+x
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and arr[nz][ny][nx]==0:
                arr[nz][ny][nx] = 1
                q.append((nz,ny,nx))

for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x]==0:
                print(-1)
                exit(0)



print(day-1)
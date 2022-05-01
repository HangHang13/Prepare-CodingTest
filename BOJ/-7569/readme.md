# 😇BOJ 7569 토마토

## 👺필요한 개념

- z축 활용법 (**처음알음**)
- bfs기본


## 👺풀이과정

- 3차원으로 배열을 생각해야한다.

## 👺코드

```python
import collections
#sys.stdin = open('input.txt')

dy=[-1,1,0,0,0,0]
dx=[0,0,1,-1,0,0]
dz=[0,0,0,0,-1,1]
M,N,H=map(int,input().split())
arr=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

#1익은토마토가 있는 좌표
q=collections.deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x]==1:
                q.append((z,y,x))
date=0
#2bfs로 토마토 익히기 z축까지 고려
while q:
    cnt= len(q)
    date+=1 #날짜에 1씩 더해줌
    for _ in range(cnt):
        z,y,x = q.popleft()
        for i in range(6):
            nz=z+dz[i]
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=nz<H and 0<=nx<M and 0<=ny<N and arr[nz][ny][nx]==0:
                arr[nz][ny][nx] = 1
                q.append((nz,ny,nx))
           
                
#3종료후 안익은 토마토 있는 경우 체크
for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x]==0:
                print(-1)
                exit(0) #for문 바로 종료
print(date-1)

```


# ๐BOJ 7569 ํ ๋งํ 

## ๐บํ์ํ ๊ฐ๋

- z์ถ ํ์ฉ๋ฒ (**์ฒ์์์**)
- bfs๊ธฐ๋ณธ


## ๐บํ์ด๊ณผ์ 

- 3์ฐจ์์ผ๋ก ๋ฐฐ์ด์ ์๊ฐํด์ผํ๋ค.

## ๐บ์ฝ๋

```python
import collections
#sys.stdin = open('input.txt')

dy=[-1,1,0,0,0,0]
dx=[0,0,1,-1,0,0]
dz=[0,0,0,0,-1,1]
M,N,H=map(int,input().split())
arr=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

#1์ต์ํ ๋งํ ๊ฐ ์๋ ์ขํ
q=collections.deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x]==1:
                q.append((z,y,x))
date=0
#2bfs๋ก ํ ๋งํ  ์ตํ๊ธฐ z์ถ๊น์ง ๊ณ ๋ ค
while q:
    cnt= len(q)
    date+=1 #๋ ์ง์ 1์ฉ ๋ํด์ค
    for _ in range(cnt):
        z,y,x = q.popleft()
        for i in range(6):
            nz=z+dz[i]
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=nz<H and 0<=nx<M and 0<=ny<N and arr[nz][ny][nx]==0:
                arr[nz][ny][nx] = 1
                q.append((nz,ny,nx))
           
                
#3์ข๋ฃํ ์์ต์ ํ ๋งํ  ์๋ ๊ฒฝ์ฐ ์ฒดํฌ
for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x]==0:
                print(-1)
                exit(0) #for๋ฌธ ๋ฐ๋ก ์ข๋ฃ
print(date-1)

```


# ๐BOJ 2636 ์น์ฆ

## ๐บํ์ํ ๊ฐ๋

- BFS
- ํ์


## ๐บํ์ด๊ณผ์ 

- bfs๋ฅผ ๋๋ ค์ ์น์ฆ๋ฅผ ๋ฐ๊ฒฌํ๋ฉด ์์ ๋ฉด์ ๊ทธ ์ซ์๋งํผ ์นด์ดํธ๋ฅผ ํ๋ค.
- ๊ทธ๋ฆฌ๊ณ  while ๋ฌธ์ ์ฌ์ฉํด์ ์๊ฐ์ ์ฒดํฌํด์ค๋ค.

## ๐บ์ฝ๋

```python
#import sys
import collections
#sys.stdin = open('input.txt')

dy=[1,-1,0,0]
dx=[0,0,1,-1]
def bfs():
    q=collections.deque()
    q.append((0,0))
    vis[0][0]=1
    cnt=0
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<m and vis[ny][nx]==0:
                
                #์น์ฆ๊ฐ ์๋๊ฒฝ์ฐ
                if arr[ny][nx]==0:
                    #๋ฐฉ๋ฌธํ์
                    vis[ny][nx]=1
                    #ํ์ฝ์
                    q.append((ny,nx))
                    
                    #์น์ฆ์ธ ๊ฒฝ์ฐ
                elif arr[ny][nx]==1:
                    #์น์ฆ๋ฅผ ๋น์
                    arr[ny][nx]=0
                    #๋ฐฉ๋ฌธํ์
                    vis[ny][nx]=1
                    #๋น์ธ ์น์ฆ๋งํผ ์นด์ดํธ
                    cnt+=1
    #ํ ํ๋น ๋น์ ์น์ฆ๋ฅผ ์ฒดํฌํด์ฃผ๊ธฐ
    ko.append(cnt)
    return cnt

#์ธ๋ก, ๊ฐ๋ก
n , m = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
#์น์ฆ ๋น์ ๊ฐฏ์ ๋ฆฌ์คํธ
ko=[]
#์๊ฐ
time=0
while 1:
    #์๊ฐ 1์ฉ ์ฆ๊ฐ
    time +=1
    #๋ฐฉ๋ฌธ๋ฆฌ์คํธ ์ด๊ธฐํ, arr์ด ๋ฐ๋์ด ์๊ธฐ ๋๋ฌธ์
    vis = [[0] * m for _ in range(n)]
    cnt = bfs()
    #๋์ด์ ๋น์ผ ์น์ฆ๊ฐ ์๋ ๊ฒฝ์ฐ break
    if cnt==0:
        #์๊ฐ ์ทจ์
        time-=1
        break

print(time) #๋ค ๋น์ ์๊ฐ
print(ko[-2]) #๋น๊ธฐ ํ์๊ฐ์  ์น์ฆ์ ๊ฐฏ์
```


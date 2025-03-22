# 😇BOJ 2636 치즈

## 👺필요한 개념

- BFS
- 탐색


## 👺풀이과정

- bfs를 돌려서 치즈를 발견하면 없애면서 그 숫자만큼 카운트를 한다.
- 그리고 while 문을 사용해서 시간을 체크해준다.

## 👺코드

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
                
                #치즈가 아닌경우
                if arr[ny][nx]==0:
                    #방문표시
                    vis[ny][nx]=1
                    #큐삽입
                    q.append((ny,nx))
                    
                    #치즈인 경우
                elif arr[ny][nx]==1:
                    #치즈를 녹임
                    arr[ny][nx]=0
                    #방문표시
                    vis[ny][nx]=1
                    #녹인 치즈만큼 카운트
                    cnt+=1
    #한 회당 녹은 치즈를 체크해주기
    ko.append(cnt)
    return cnt

#세로, 가로
n , m = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
#치즈 녹은 갯수 리스트
ko=[]
#시간
time=0
while 1:
    #시간 1씩 증가
    time +=1
    #방문리스트 초기화, arr이 바뀌어 있기 때문에
    vis = [[0] * m for _ in range(n)]
    cnt = bfs()
    #더이상 녹일 치즈가 없는 경우 break
    if cnt==0:
        #시간 취소
        time-=1
        break

print(time) #다 녹은 시간
print(ko[-2]) #녹기 한시간전 치즈의 갯수
```


# 적록색약 다국어한국어  

| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :---- | :---- | :-------- | :-------- |
| 1 초      | 128 MB      | 32858 | 18984 | 14786     | 57.272%   |

## 문제

적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

```
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
```

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

## 출력

적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

## 예제 입력 1 복사

```
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
```

## 예제 출력 1 복사

```
4 3
```



## 코드

- 섬문제 비슷하게 빠져나오면 카운트해주기 !

```python
import sys
sys.setrecursionlimit(1000000) #안하면 리커시브 에러남
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

#적록 색약 아닌경우
cnt1=0
for y in range(n):
    for x in range(n):
        if vis[y][x] == False:
            dfs(y,x) #빠져나오는 경우 카운트
            cnt1+=1

cnt2=0
#적록색약인경우 R을 G로 인식
for y in range(n):
    for x in range(n):
        if arr[y][x] == 'R':
            arr[y][x] = 'G'

vis = [[False]* n for _ in range(n)]

#적록 색약인 경우
for y in range(n):
    for x in range(n):
        if vis[y][x] == False:
            dfs(y,x) #빠져나오는 경우 카운트
            cnt2+=1

print(cnt1,cnt2)


```


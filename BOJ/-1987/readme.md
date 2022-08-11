# 알파벳 다국어한국어  

| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :---- | :---- | :-------- | :-------- |
| 2 초      | 256 MB      | 74977 | 23816 | 14640     | 28.892%   |

## 문제

세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

## 입력

첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

## 출력

첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

## 예제 입력 1 복사

```
2 4
CAAB
ADCB
```

## 예제 출력 1 복사

```
3
```

## 예제 입력 2 복사

```
3 6
HFDFFB
AJHGDH
DGAGEH
```

## 예제 출력 2 복사

```
6
```

## 예제 입력 3 복사

```
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
```

## 예제 출력 3 복사

```
10
```

## 풀이

```python
import sys

r,c = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
dy=[1,-1,0,0]
dx=[0,0,-1,1]

ans = 1
# print(arr)
def bfs(y,x):
    global ans
    q = set([(y,x,arr[y][x])]) //리스트 형식은 시간초과 set쓰자
    while q:
        y,x,target = q.pop()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=nx<c and 0<=ny<r and arr[ny][nx] not in target:
                q.add((ny,nx, target+arr[ny][nx])) //타겟에 계속 붙여준다 ABCD...
                ans = max(ans, len(target)+1) //타겟은 처음시작할때부터 1이므로 +1더해준다

bfs(0,0)
print(ans)


//입력
CAAB
ADCB

//타겟출력
C
CA
CA
CAD


//입력
HFDFFB
AJHGDH
DGAGEH

//타겟출력
H
HF
HA
HFJ
HFJA
HAD
HAJ
HFD
HAJG
HADG
HAJF
HFJG
HAJGD
HFJGA
HFJAD
HFJADG
HAJFD
HADGJ
HFJGD
HADGJF
HFJGDA
```

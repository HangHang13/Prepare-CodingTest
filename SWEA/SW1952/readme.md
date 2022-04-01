# 😇SWEA1952 수영장

## 👺필요한 개념

- dfs로 순회하기


## 👺풀이과정

- dfs로 분할정복하기
- dfs로 각 일일권, 월간권, 분기권, 년간권 정해주는게 떠오르지 않았다.
- 동적 나이내믹의 경우 일일히 비교해서 값싼것으로 넣는다.
- 마지막12월달에 정산해보고 그게 년간권보다 적은경우 년간권으로 교체한다.

## 👺코드

1. 분할정복으로 풀기

```python
import sys
sys.stdin = open('input.txt')

def DFS(n,ssum):

    global ans

    # 종료조건
    if n>12:
        #최솟값 찾기
        if ans > ssum:
            ans = ssum
        return
    #일일권
    DFS(n+1,ssum+lst[n]*day)
    #월간권
    DFS(n+1,ssum+mon)
    #분기권
    DFS(n+3,ssum+mon3)
    #년간권
    DFS(n+12, ssum+year)

#케이스입력
num = int(input())

for tc in range(1,num+1):
    day, mon, mon3, year = map(int, input().split())
    lst=list(map(int, input().split()))
    lst=[0]+lst
    ans=9999999
    DFS(1,0)

    print(f'#{tc} {ans}')


```

2. 동적다이내믹으로 풀기

```python
#케이스입력
num = int(input())

for tc in range(1,num+1):
    day, mon, mon3, year = map(int, input().split())
    lst=list(map(int, input().split()))
    lst=[0]+lst
    d=[0]*13
    #print(f'day: {day} mon: {mon} mon3: {mon3} year: {year}')
    #print(lst)

    for a in range(1,13):
        mmin = d[a-1]+lst[a]*day
        mmin = min(mmin, d[a-1]+mon)
        if a>=3:
            mmin=min(mmin, d[a-3]+mon3)
        if a>=12:
            mmin=min(mmin, d[a-12]+year)
        d[a]=mmin

    print(f'#{tc} {d[-1]}')
```


# ๐SWEA1952 ์์์ฅ

## ๐บํ์ํ ๊ฐ๋

- dfs๋ก ์ํํ๊ธฐ


## ๐บํ์ด๊ณผ์ 

- dfs๋ก ๋ถํ ์ ๋ณตํ๊ธฐ
- dfs๋ก ๊ฐ ์ผ์ผ๊ถ, ์๊ฐ๊ถ, ๋ถ๊ธฐ๊ถ, ๋๊ฐ๊ถ ์ ํด์ฃผ๋๊ฒ ๋ ์ค๋ฅด์ง ์์๋ค.
- ๋์  ๋์ด๋ด๋ฏน์ ๊ฒฝ์ฐ ์ผ์ผํ ๋น๊ตํด์ ๊ฐ์ผ๊ฒ์ผ๋ก ๋ฃ๋๋ค.
- ๋ง์ง๋ง12์๋ฌ์ ์ ์ฐํด๋ณด๊ณ  ๊ทธ๊ฒ ๋๊ฐ๊ถ๋ณด๋ค ์ ์๊ฒฝ์ฐ ๋๊ฐ๊ถ์ผ๋ก ๊ต์ฒดํ๋ค.

## ๐บ์ฝ๋

1. ๋ถํ ์ ๋ณต์ผ๋ก ํ๊ธฐ

```python
import sys
sys.stdin = open('input.txt')

def DFS(n,ssum):

    global ans

    # ์ข๋ฃ์กฐ๊ฑด
    if n>12:
        #์ต์๊ฐ ์ฐพ๊ธฐ
        if ans > ssum:
            ans = ssum
        return
    #์ผ์ผ๊ถ
    DFS(n+1,ssum+lst[n]*day)
    #์๊ฐ๊ถ
    DFS(n+1,ssum+mon)
    #๋ถ๊ธฐ๊ถ
    DFS(n+3,ssum+mon3)
    #๋๊ฐ๊ถ
    DFS(n+12, ssum+year)

#์ผ์ด์ค์๋ ฅ
num = int(input())

for tc in range(1,num+1):
    day, mon, mon3, year = map(int, input().split())
    lst=list(map(int, input().split()))
    lst=[0]+lst
    ans=9999999
    DFS(1,0)

    print(f'#{tc} {ans}')


```

2. ๋์ ๋ค์ด๋ด๋ฏน์ผ๋ก ํ๊ธฐ

```python
#์ผ์ด์ค์๋ ฅ
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


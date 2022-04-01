import sys
sys.stdin = open('input.txt')

def DFS(n,ssum):

    global ans

    # 종료조건
    if n>12:
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




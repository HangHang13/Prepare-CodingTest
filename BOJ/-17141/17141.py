import sys
import collections
import itertools
sys.stdin = open('input.txt')

t= int(input())
q=collections.deque([])
dy=[1,-1,0,0]
dx=[0,0,1,-1]

for _ in range(1):
    n,m= map(int, input().split())
    arr=[]
    for _ in range(n):
        arr.append(list(map(int, input().split())))


    sts=[]
    for y in range(n):
        for x in range(n):
            if arr[y][x]==2:
                sts.append((y,x))

    sta=[]
    _time= n
    for a in itertools.combinations(sts,m):

        vis = [[-1] * n for _ in range(n)]

        for b in a:
            vis[b[0]][b[1]]=0
            q.append(b)

        while q:
            y,x = q.popleft()
            for i in range(4):
                ny=y+dy[i]
                nx=x+dx[i]
                if 0<=ny<n and 0<=nx<n and arr[ny][nx] != 1 and (vis[ny][nx]==-1 or vis[ny][nx]>vis[y][x]+1):
                    vis[ny][nx]= vis[y][x]+1
                    q.append((ny,nx))
                    _time-=1

        _time=vis[y][x]

        print()

        for b in arr:
            for a in b:
                print(a, end=" ")
            print()









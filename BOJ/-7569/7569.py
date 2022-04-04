import sys
import collections
sys.stdin = open('input.txt')

dy=[1,-1,0,0]
dx=[0,0,1,-1]
def bfs1(y,x):
    global cnt
    q=collections.deque()
    q.append((y,x))
    #vis[y][x]=1
    cnt=0
    while q:
        cnt += 1
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]==0:
                arr[ny][nx]=1
                #vis[ny][nx]=1

                q.append((ny,nx))
def bfs2(y,x):
    global cnt
    q=collections.deque()
    q.append((y,x))
    #vis[y][x]=1
    cnt=0
    while q:
        cnt += 1
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if N<=ny<N*H and 0<=nx<M and arr[ny][nx]==0:
                arr[ny][nx]=1

                q.append((ny,nx))



t= int(input())
for _ in range(2):
    M,N,H=map(int,input().split())
    arr=[]
    for _ in range(H):
        for _ in range(N):
            arr.append(list(map(int, input().split())))


    #1토마토가 있는 좌표
    route=[]
    for y in range(N*H):
        for x in range(M):
            if arr[y][x]==1:
                route.append((y,x))

    #방문처리
    vis=[[0]*M for _ in range(N)]
    print(route)


    y, x = route[0]
    bfs2(y,x)
    bfs1(2,2)

    for a in arr:
        for b in a:
            print(b,end=" ")
        print()

    #안익은 토마토 있는경우
    for y in range(N):
        for x in range(M):
            if arr[y][x] ==-1:
                cnt=-1
    print(cnt)
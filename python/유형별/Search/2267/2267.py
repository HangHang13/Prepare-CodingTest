import collections

n=int(input())


arr = []

for i in range(n):
    arr.append(list(map(int, input())))
vis = [[0]* n for _ in range(n)]


dx=[0,0,1,-1]
dy=[1,-1,0,0]






def bfs(arr , a,b):
    n= len(arr)

    q= collections.deque()
    q.append((a,b))

    arr[a][b]=0
    cnt=1

    while q:
        y,x =q.popleft()
        for i in range(4):
            ny= y+dy[i]
            nx=x +dx[i]

            if 0<=nx<n and 0<=ny<n:
                if arr[ny][nx] == 1:
                    arr[ny][nx] = 0
                    q.append((ny,nx))
                    cnt+=1
            else:
                continue
    return cnt


lst=[]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            lst.append(bfs(arr, i,j))

lst.sort()

print(len(lst))
for i in range(len(lst)):
    print(lst[i])

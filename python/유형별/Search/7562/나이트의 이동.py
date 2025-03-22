import sys
import collections
input = sys.stdin.readline

n=int(input())

dy=[2,2,-2,-2,1,-1,1,-1]
dx=[1,-1,1,-1,2,2,-2,-2]
for _ in range(n):
    l = int(input())

    arr = [[0]*l for _ in range(l)]
    q= collections.deque()
    y,x = map(int, input().split())
    q.append((y,x))
    ty,tx = map(int, input().split())
    while q:
        y,x =q.popleft()
        if y==ty and x==tx:
            print(arr[ty][tx])
            break
        for k in range(len(dx)):
            ny=y+dy[k]
            nx=x+dx[k]
            if 0<=ny<l and 0<=nx<l and arr[ny][nx]==0:
                arr[ny][nx] = arr[y][x] +1
                q.append((ny,nx))
            else:
                continue





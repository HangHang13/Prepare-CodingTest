import sys

r,c = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(r)]
dy=[1,-1,0,0]
dx=[0,0,-1,1]

ans = 1
# print(arr)
def bfs(y,x):
    global ans
    q = set([(y,x,arr[y][x])])
    while q:
        y,x,target = q.pop()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=nx<c and 0<=ny<r and arr[ny][nx] not in target:
                q.add((ny,nx, target+arr[ny][nx]))
                ans = max(ans, len(target)+1)
        print(target)

bfs(0,0)
print(ans)




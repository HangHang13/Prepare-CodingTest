import collections
q = collections.deque([])
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
y, x = 0, 0
q.append((y, x))
dy = [1,0]
dx = [0,1]
t=0
vis = [[False] *n for _ in range(n)]
while q:
    y, x = q.popleft()
    if arr[y][x] == -1:
        t=1
        break
    step = arr[y][x]
    for k in range(2):
        ny = y + dy[k]*step
        nx = x + dx[k]*step
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if not vis[ny][nx]:
            vis[ny][nx] = True
            q.append((ny,nx))


if t==0:
    print("Hing")
else:
    print("HaruHaru")
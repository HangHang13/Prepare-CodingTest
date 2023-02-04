import collections
q=collections.deque([])

n,m = map(int, input().split())

arr= []

for _ in range(n):
    arr.append(list(input().rstrip()))


print(arr)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
q.append((0,0))
buffer = []
while q:
    y,x = q.popleft()
    for a in range(4):
        ny = y+dy[a]
        nx = x+dx[a]
        if 0<=ny<n and 0<=nx<m and arr[ny][nx] != '2':
            arr[ny][nx] = '2'
            q.append((ny,nx))

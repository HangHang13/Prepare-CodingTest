
n, m = map(int ,input().split())

arr = [[0 ]* m for _ in range(m)]
x ,y = 0 ,0
k= 0
dx = [0, -1, 0, 1]
dy = [ 1, 0, -1, 0]
z = 0
for _ in range(n):
    a, b = input().split()
    if a == 'MOVE':
        y += dy[k] * int(b)
        x += dx[k] * int(b)
    else:
        if b == 0:
            k = k-1 if k-1 !=-1 else 3
        else: k = k+1 if k+1 != 4 else 0

    print("k, x , y = ",k, x,y )
    if x < 0 or x > m or y < 0 or y > m:
        z = 1
        break

if z == 1:
    print(-1)
else:
    print(x, y)

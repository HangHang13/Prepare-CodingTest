k = int(input())
n = int(input())


def isValid(y, x):
    if y >= 0 and y < k and x >= 0 and x < k:
        return True
    else:
        False


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# start_y, start_x = k // 2, k // 2
arr = [[0] * k for _ in range(k)]

start_y,start_x = 0,0
idx=0
cnt= k**2
arr[start_y][start_x] = cnt
cnt-=1

ty=0
tx=0
while cnt>0:
    ny = start_y +dy[idx]
    nx = start_x +dx[idx]
    if 0 <= nx < k and 0 <= ny < k and not arr[ny][nx]:
        arr[ny][nx] = cnt
        if cnt == n:
            ty,tx = ny,nx
        start_y, start_x = ny,nx
        cnt-=1
    else:
        idx = (idx+1)%4

for a in arr:
    print(*a)
print(ty+1,tx+1)
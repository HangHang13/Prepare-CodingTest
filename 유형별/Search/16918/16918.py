import sys
import collections

# input = sys.stdin.readline

q = collections.deque()
r, c, n = map(int, input().split())

arr = []

for i in range(r):
    arr.append(list(input()))

for a in arr:
    for b in a:
        print(b, end="")
    print()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 1


def boom(y, x, cnt):
    if cnt %3 ==0 :

        q.append((y, x))
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < r and 0 <= nx < c:
                arr[y][x] = '.'
                arr[ny][nx] = '.'


con=1
while 1:

    for y in range(r):
        for x in range(c):
            if arr[y][x] == 'O':
                boom(y, x, cnt)
            if arr[y][x] == '.':
                arr[y][x] = 'O'

    print()
    for a in arr:
        for b in a:
            print(b, end=" ")
        print()

    cnt += 1
    con +=1
    if con == n:
        break


print('===========')
for a in arr:
    for b in a:
        print(b, end=" ")
    print()

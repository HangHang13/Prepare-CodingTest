import sys
import collections

# input = sys.stdin.readline

r, c, n = map(int, input().split())

arr = []

for i in range(r):
    arr.append(list(input()))

def check():
    for y in range(r):
        for x in range(c):
            if arr[y][x] == 'O':
                q.append((y, x))


def boom():
    while q:
        y, x = q.popleft()
        arr[y][x] = '.'
        if 0 <= y - 1:
            arr[y - 1][x] = '.'
        if y + 1 < r:
            arr[y + 1][x] = '.'
        if 0 <= x - 1:
            arr[y][x - 1] = '.'
        if x + 1 < c:
            arr[y][x + 1] = '.'


def c4():
    for y in range(r):
        for x in range(c):
            if arr[y][x] == '.':
                arr[y][x] = 'O'


n -= 1

while n:
    q = collections.deque()
    check()
    c4()
    n -= 1
    if n == 0:
        break
    boom()
    n -= 1
#
# for a in arr:
#     for b in a:
#         print(b, end="")

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end='')
    print()
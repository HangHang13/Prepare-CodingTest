import sys
import collections

sys.stdin = open('input.txt', 'r')
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
q = collections.deque()
n = int(input())
std = [list(map(int, input().split())) for _ in range(n)]
grid = [[0] for _ in range(n)]
arr = []

print(grid)

vis = [[False] * n for _ in range(n)]


def bfs(num):
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not vis[ny][nx] and (abs(ny - y) + abs(nx - x)) == 1:
                vis[ny][nx] = num
                q.append((ny, nx))
            else:
                continue
for a in range(n):
    bfs(std[a][0])


for a in vis:
    for b in a:
        print(b, end=" ")
    print()
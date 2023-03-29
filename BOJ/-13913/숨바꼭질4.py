import sys
# input = sys.stdin.readline
import collections

n, k = map(int, input().split())
vis = [0 for _ in range(100001)]
count = [0 for _ in range(100001)]


def bfs(v):
    q = collections.deque([v])
    while q:
        v = q.popleft()
        if v == k:
            print(vis[v])
            return count
        for i in (v - 1, v + 1, v * 2):
            if 0 <= i <= 100000 and vis[i] == 0:
                count[i] = v
                vis[i] = vis[v] + 1
                q.append(i)

def path(x):
    a = []
    temp = x

    for _ in range(vis[x] + 1):
        a.append(temp)
        temp = count[temp]

    return a[::-1]

(bfs(n))
print(*path(k))
print(count)
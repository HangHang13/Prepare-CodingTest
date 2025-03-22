import collections
import sys

sys.setrecursionlimit(300000)

q = collections.defaultdict(list)

k = int(input())
vis = [0] * (k + 1)

a, b = map(int, input().split())
t = int(input())

for j in range(t):
    x, y = map(int, input().split())
    q[x] += [y]
    q[y] += [x]
cnt = 0


def dfs(n):
    for i in q[n]:
        if vis[i] == 0:
            vis[i] = vis[n] + 1
            dfs(i)


dfs(a)
# print(q)
# print(vis[b-1])
# print(vis)
if vis[b] != 0:
    print(vis[b])
else:
    print(-1)

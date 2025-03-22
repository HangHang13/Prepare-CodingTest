a, k = map(int, input().split())
import collections
q = collections.deque([(a, 0)])

_max = 100001
_min = 0
vis = [False] * _max
ans = []
while q:
    n, t = q.popleft()
    vis[n] = True

    if n == k:
        ans.append(t)
    if n * 2 < _max and not vis[n * 2]:
        q.append((n * 2, t))
    if n + 1 < _max and not vis[n + 1]:
        q.append((n + 1, t + 1))
    if _min <= n - 1 and not vis[n - 1]:
        q.append((n - 1, t + 1))

print(min(ans))

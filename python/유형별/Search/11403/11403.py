import collections

n=int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
trr = [[0]* n for _ in range(n)]


def bfs(a):
    vis = [False] * (n+1)
    q = collections.deque()
    q.append(a)
    while q:
        t = q.popleft()
        for i in range(n):
            if not vis[i] and arr[t][i] == 1:
                q.append(i)
                vis[i] = True
                trr[a][i] = 1
cnt=0
for a in range(n):
    bfs(a)

for i in trr:
    print(*i)


import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

lst = collections.defaultdict(list)


n,m = map(int, input().split())

for _ in range(m):
    a,b = map(int, input().split())

    lst[a]+=[b]
    lst[b]+=[a]


vis=[0] * (n)
arrive = False
def dfs(a, dep):
    global arrive
    vis[a] = 1
    if dep ==5:
        arrive = True
        return
    for i in lst[a]:
        if vis[i] == 0:
            dfs(i, dep+1)
    # vis[a]=0

for i in range(n):
    dfs(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
import sys
import collections
input = sys.stdin.readline

t = int(input())
def dfs(n,cnt):
    vis[n]=1
    for i in arr[n]:
        if vis[i] == 0:
            cnt = dfs(i, cnt+1)
    return cnt
for _ in range(t):
    n,m = map(int, input().split())
    arr = collections.defaultdict(list)
    for _ in range(m):
        a,b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    vis = [0] * (n+1)
    cnt =dfs(1,0)
    print(cnt)



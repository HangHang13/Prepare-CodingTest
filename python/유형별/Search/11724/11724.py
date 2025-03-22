import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


n,m = map(int,input().split())

arr=[[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())

    arr[u].append(v)
    arr[v].append(u)

vis = [0]*(n+1)
def dfs(n):
    vis[n]=1
    for i in arr[n]:
        if vis[i]==0:
            dfs(i)

cnt=0
for i in range(1,n+1):
    if vis[i]==0:
        dfs(i)
        cnt+=1
print(cnt)

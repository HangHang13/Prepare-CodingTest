n= int(input())
k = int(input())
import collections
q = collections.defaultdict(list)
for _ in range(k):
    a,b = map(int, input().split())


    q[a]+=[b]
    q[b]+=[a]





vis = [0] * (n+1)

def dfs(n):
    vis[n] = 1

    for a in q[n]:

        if vis[a] == 0:
            dfs(a)

dfs(1)
cnt=0
for a in vis:
    if a == 1:
        cnt+=1
print(cnt-1)
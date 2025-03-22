import collections
import sys
def bfs(a):



n , m = map(int, input().split())
grp = [[] for i in range(n+1)]
for _ in range(n):
    a,b,c = map(int, input().split())
    grp[a].append((b,c))
    grp[b].append((a,c))

x,y = map(int, input().split())
mm = 1
LL = 10000000

print(grp)
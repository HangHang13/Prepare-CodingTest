import sys
import collections
# input =sys.stdin.readline

# cos1=[]
cos2=[]

def dfs(n, cos1=[]):
    cos1.append(n)
    for i in lst[n]:
        if i not in cos1:
            cos1 = dfs(i,cos1)
    return cos1
def bfs(n):
    q.append(n)
    cos2 = [n]
    while q:
        a = q.popleft()
        for i in lst[a]:
            if i not in cos2:
                q.append(i)
                cos2.append(i)
    return cos2



n,m,v = map(int , input().split())

vis1=[0] *(m+1)
vis2=[0]*(m+1)
q=collections.deque()
lst = collections.defaultdict(list)
for _ in range(m):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for node in list(lst):
    lst[node] = sorted(lst[node])







print(' '.join(map(str, dfs(v)))+' ')
print(' '.join(map(str,bfs(v)))+' ')
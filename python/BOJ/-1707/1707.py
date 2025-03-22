import sys
input = sys.stdin.readline
k= int(input())
import collections
q=collections.deque()
def bfs(start):
    q=collections.deque([start])
    vis[start] =1

    while q:
        v= q.popleft()
        for i in arr[v]:
            if vis[v] ==0:
                q.append(i)
                vis[i]=-vis[v]
            elif vis[i] == vis[v]:
                return False
    return True


for _ in range(k):
    arr = collections.defaultdict(list)
    v,e = map(int, input().split())
    vis=[0]*(v+1)
    res= True
    for _ in range(e):
        a,b= map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1,v+1):
        if vis[i]==0:
            if not bfs(i):
                res=False
                break
    print('yES' if res else 'NO')
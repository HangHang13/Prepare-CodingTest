from collections import deque


q= deque()

n,k = map(int,input().split())

d = [1,-1,'j']
cnt=0
q.append(n)
_max = 100000
dist = [0] * (_max+1)
while q:
    a= q.popleft()
    if a == k:
        print(dist[a])
        break
    for i in (a-1,a+1,a*2):
        if 0<=i<=_max and not dist[i]:
            dist[i] = dist[a]+1
            q.append(i)





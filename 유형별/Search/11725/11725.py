n=int(input())

import collections

q= collections.defaultdict(list)

for _ in range(n-1):
    a,b=map(int, input().split())

    q[a]+=[b]
    q[b]+=[a]


t= collections.deque()

t.append(1)
vis = [0]*(n+1)

while t:
    a=t.popleft()
    for i in q[a]:
        if vis[i]==0:
            vis[i]=a
            t.append(i)

for i in vis[2:]:
    print(i)
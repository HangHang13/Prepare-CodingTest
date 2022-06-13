import sys
import collections

sys.stdin = open('input.txt')


def DFS(graph, v, visited):
    visited[y][x] =True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[y][x]:
            DFS(graph, i, visited)

# 길이받기
n = int(input())

# 그래프 받기

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

#방문경로
vis = [[0]*n for _ in range(n)]

#queue스택

#좌표저장

sts = collections.deque([])

for y in range(n):
    for x in range(n):
        if arr[y][x] ==1:
            sts.append((y,x))

print(sts)

dy=[1,-1,0,0]
dx=[0,0,1,-1]


# while sts:
#     vis = [[0] * n for _ in range(n)]
#     y,x = sts.popleft()

#     for i in range(4):
#         ny = y+ dy[i]
#         nx = x+ dx[i]

#         if 0>ny or ny>=n or 0>nx or nx>=n or arr[ny][nx] ==1:
#             continue
#         else:
#             vis[ny][nx]=vis[ny][nx]+1
#             sts.append((ny,nx))

for a in sts:
    DFS(arr,a,vis)


for a in vis:
    for b in a:
        print(b, end=" ")
    print()
print()
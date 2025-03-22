import sys
INF = int(1e9)
from heapq import heappush, heappop
input = sys.stdin.readline

n=int(input())
m=int(input())

arr = [[] for _ in range(n+1)]
distance = [INF] * (n+1)   # 거리 테이블용

for _ in range(m):
    a,b,c = map(int , input().split())

    arr[a].append([b,c])


start, end = map(int,input().split())

def dijkstra(start):
    distance[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if distance[n] < w:
            continue
        for n_n, wei in arr[n]:
            n_w = w + wei
            if distance[n_n] > n_w:
                distance[n_n] = n_w
                heappush(heap, [n_w, n_n])
dijkstra(start)
print(distance[end])

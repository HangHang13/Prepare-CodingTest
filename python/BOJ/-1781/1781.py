import heapq
import sys


n = int(input())

scedule = []
for _ in range(n):
    dead , noodle = map(int, input().split())
    scedule.append((dead,noodle))




print(scedule)


scedule.sort()
q=[]
for dead, noodle in scedule:
    heapq.heappush(q,noodle)
    print(len(q))
    if dead<len(q):
        heapq.heappop(q)

    print(q)

print(sum(q))
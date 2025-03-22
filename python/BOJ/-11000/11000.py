import sys
import heapq
sys.stdin = open('input.txt')

n = int(input())

q = []


for _ in range(n):
    q.append(list(map(int, input().split())))

q.sort()
print(q)
hq = []
heapq.heappush(hq, q[0][1])

for i in range(1,n):
    if hq[0] <= q[i][0]:
        heapq.heappop(hq)
        print(hq)
    heapq.heappush(hq,q[i][1])
    print(hq)

print(len(hq))




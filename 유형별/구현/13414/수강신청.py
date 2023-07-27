
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
from collections import deque

q = dict()

for _ in range(m):
    t = input().strip()
    if t in q.keys():
        del q[t]
        q[t] = 1


    if t not in q.keys():
        q[t] = 1


s = list(q)
for i in range(n):
    try:
        print(s[i])
    except:
        pass

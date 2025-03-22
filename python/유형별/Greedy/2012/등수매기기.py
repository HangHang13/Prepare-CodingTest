import sys
input = sys.stdin.readline

n = int(input())
lst = [i for i in range(1,n+1)]

q = []
for _ in range(n):

    t = int(input())
    q.append(t)
q.sort()
cnt = 0
for i in range(n):
    cnt += abs(lst[i] - q[i])
print(cnt)



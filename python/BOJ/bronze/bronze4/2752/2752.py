import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

aa = []

aa.append(a)
aa.append(b)
aa.append(c)
aa.sort()
for a in aa:
    print(a, end=" ")



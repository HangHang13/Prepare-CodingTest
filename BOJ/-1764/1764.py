import sys
input = sys.stdin.readline

n,m = map(int, input().split())

nolis=set()
for _ in range(n):
    nolis.add(input().strip())
nosee=set()
for _ in range(m):
    nosee.add(input().strip())

res= sorted(list(nolis & nosee))

print(len(res))
# print(res)
for i in res:
    print(i)
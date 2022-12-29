import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt", "rt")

n = int(input())

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
# arr.sort(key=lambda x: x[1], reverse=True)
arr.sort()
cnt = 0
vis = [False] * (1000 + 1)
print(arr)
do=[]
first = arr[-1][0]
while True:
    if first == 0:
        break
    while arr and arr[-1][0] >=first:
        do.append(arr.pop()[1])
    first -=1
    if not do:
        continue
    print(do)

print(sum(do))
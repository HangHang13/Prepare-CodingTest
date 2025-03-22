import sys
from itertools import combinations


n,m = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(n))
res=99999
house=[]
chicken=[]


for y in range(n):
    for x in range(n):
        if arr[y][x] ==1:
            house.append((y,x))
        elif arr[y][x] ==2:
            chicken.append((y,x))
        else:
            pass
# print(house, chicken)

for a in combinations(chicken, m):
    tmp = 0
    for b in house:
        chiken_len= 999
        for c in range(m):
            chiken_len = min(chiken_len, abs(b[0]-a[c][0])+abs(b[1]-a[c][1]))
        tmp+=chiken_len
    res = min(res,tmp)
print(res)
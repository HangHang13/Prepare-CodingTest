n=int(input())
arr= []
import sys
sys.setrecursionlimit(100000)


for _ in range(n):
    arr.append(list(map(int, input().split())))


#
# for y in range(n):
#     for x in range(n):
#         if arr[y][x] <=n:
#             arr[y][x]=0
#         else:
#             continue


def dfs(y,x,h):
    if y<0 or y>=n or x<0 or x>=n or arr[y][x]<=h or vis[y][x]==True:
        return
    vis[y][x] = True


    dfs(y+1,x,h)
    dfs(y,x+1,h)
    dfs(y-1,x,h)
    dfs(y,x-1,h)



cnt=0

# for y in range(n):
#     for x in range(n):
#         if arr[y][x] !=0:
#             dfs(y,x)
#             cnt+=1
#
# print(cnt)

for h in range(101):
    _cnt=0
    vis = [[False for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if arr[y][x] >h and not vis[y][x]:
                dfs(y,x,h)
                _cnt+=1
    cnt = max(cnt, _cnt)

print(cnt)
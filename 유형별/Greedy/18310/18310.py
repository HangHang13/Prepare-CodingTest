import sys
input = sys.stdin.readline
n = int(input())


arr = list(map(int, input().split()))
arr.sort()
mid = len(arr)//2
vis = [0] * n
ans = []
for i in range(mid-1 , mid+1):
    cnt = arr[i]
    con = 0
    for j in arr:
        con += abs(cnt - j)
    vis[i] = con
for i in range(len(vis)):
    if vis[i] != 0:
        ans.append(arr[i])
print(min(ans))
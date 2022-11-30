import sys
input = sys.stdin.readline


n,k = map(int, input().split())

mod = 1000000000



arr = [[0]*n for _ in range(k)]

for i in range(n):
    arr[0][i] = 1
for i in range(k):
    arr[i][0] = i+1

for y in range(1,k):
    for x in range(1,n):
        arr[y][x] = (arr[y-1][x]+arr[y][x-1])%mod


print(arr[k-1][n-1])


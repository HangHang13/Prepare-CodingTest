import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    lst = list(input().rstrip())
    arr.append(lst)

_max = 0


def check(arr):
    global _max
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
                _max = max(cnt, _max)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
                _max = max(cnt, _max)
            else:
                cnt = 1


for y in range(n):
    for x in range(n):
        if x + 1 < n:
            arr[y][x], arr[y][x + 1] = arr[y][x + 1], arr[y][x]
            check(arr)
            arr[y][x + 1], arr[y][x] = arr[y][x], arr[y][x + 1]

        if y + 1 < n:
            arr[y][x], arr[y + 1][x] = arr[y + 1][x], arr[y][x]
            check(arr)
            arr[y + 1][x], arr[y][x] = arr[y][x], arr[y + 1][x]

print(_max)

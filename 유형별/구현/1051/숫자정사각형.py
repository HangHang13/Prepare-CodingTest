n, m = map(int, input().split())

arr = []
for _ in range(n):
    t = list(map(int, input()))
    arr.append(t)
lst = []
for y in range(n):
    for x in range(m):
        tar = arr[y][x]
        for j in range(x, m):
            if arr[y][j] == tar and y + j - x < n and j < m:
                if arr[y + j - x][x] == tar and arr[y + j - x][j] == tar:
                    lst.append((j - x + 1) ** 2)
print(max(lst))

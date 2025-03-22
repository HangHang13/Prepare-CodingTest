import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    arr = []
    for _ in range(k):
        a, b = map(int, input().split())
        arr.append([a, b])

    arr_s = sorted(arr)
    # print(*arr_s)
    tmp  = arr_s[0][1]
    res = 1

    for i in range(0, len(arr_s)):
        if arr_s[i][1] < tmp:
            tmp = arr_s[i][1]
            res += 1

    print(res)

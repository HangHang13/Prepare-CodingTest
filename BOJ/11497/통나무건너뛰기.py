n = int(input())

for _ in range(n):
    a= int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 0
    for n in range(2,a):
        res = max(res, abs(arr[n]-arr[n-2]))

    print(res)
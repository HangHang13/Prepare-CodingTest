import sys
input = sys.stdin.readline


a = input().rstrip()
b = input().rstrip()

print(a)
print(b)


ans=0

arr = [[0]* (len(b)+1) for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[i-1]:
            arr[i][j] = arr[i-1][j-1] +1
            ans = max(arr[i][j], ans)

print(ans)

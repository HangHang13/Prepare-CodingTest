


n = int(input())
lst=[]
for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a,b))

print(lst)


dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(lst[i][0]+i, n+1):
        if dp[j] < dp[i] + lst[i][1]:
            dp[j] = dp[i] + lst[i][1]
    print(dp)
print()
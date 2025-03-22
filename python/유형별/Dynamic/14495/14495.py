n=int(input())

dp=[0]*(n+1)
if n>2:
    dp[0]=1
    dp[1]=1
    dp[2]=1
elif n>1:
    dp[0]=1
    dp[1]=1
else:
    dp[0]=1
for i in range(3,n):
    dp[i]=dp[i-3]+dp[i-1]


print(dp[n-1])
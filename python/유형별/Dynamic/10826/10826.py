n=int(input())



dp=[0] * (n+1)

dp[0]=0
if n>2:
    dp[2]=1
    dp[1]=1
elif n>0:
    dp[1]=1
else:
    pass


for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]


print(dp[n])
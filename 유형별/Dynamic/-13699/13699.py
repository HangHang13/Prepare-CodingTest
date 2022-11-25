n=int(input())

dp=[0]*36
dp[0]=1
dp[1]=1
dp[2]=2


dp[0]=1

for i in range(3, n+1):
    ant= 0

    if i%2:
        for j in range(i//2):
            ant+=2*dp[j]*dp[i-j-1]
        dp[i] = ant+dp[i//2]**2
    else:
        for j in range(i//2):
            ant+=2*dp[j]*dp[i-j-1]
        dp[i]=ant
print(dp[n])
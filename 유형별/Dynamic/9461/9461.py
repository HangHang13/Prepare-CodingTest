t=int(input())
for _ in range(t):
    k= int(input())

    dp = [0] * (100)



    dp[0]=dp[1]= dp[2] = 1

    for i in range(3,k):
        dp[i] = dp[i-2]+dp[i-3]


    print(dp[k-1])

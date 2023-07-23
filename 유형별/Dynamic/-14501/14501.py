n=int(input())
t=[]
p=[]
dp=[0 for i in range(n+1)]
for _ in range(n):
   a,b = map(int, input().split())
   t.append(a)
   p.append(b)




for i in range(n):
   for j in range(i+t[i], n+1):
      if dp[j]<dp[i] + p[i]:
         dp[j] = dp[i] + p[i]
   print(dp)

print("=====================")
# for i in range(n-1, -1,-1):
#    if i+t[i] > n:
#       dp[i] = dp[i+1]
#    else:
#       dp[i] = max(dp[i+1], p[i]+dp[i])
#
#    print(dp)


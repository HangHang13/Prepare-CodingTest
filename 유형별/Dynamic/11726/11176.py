n=int(input())

s= [0] *(n+1)
s[0]=1
s[1]=2
for i in range(2,n):
    s[i] = s[i-1] + s[i-2]

print(s[-2]%10007)
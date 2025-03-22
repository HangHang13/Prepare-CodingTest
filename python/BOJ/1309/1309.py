
n= int(input())

k = [1,3] + [0]*(n-1)

for i in range(2, n+1):
    k[i] = (2*k[i-1]+k[i-2])%9901

print(k[n])


#n=0 1
#n=1 3
#n=2 7
#n=3 17
#n=4 41

# f(n)= 2*f(n-1) + f(n-2)
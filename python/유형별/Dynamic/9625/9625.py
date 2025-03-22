k= int(input())



A=[1]
B=[0]
for i in range(k):
    A.append(B[i])
    B.append(B[i] +  A[i])


print(A[-1], end=" ")
print(B[-1])
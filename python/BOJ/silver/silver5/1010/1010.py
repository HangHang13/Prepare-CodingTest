n= int(input())



import math
for _ in range(n):
    a,b = map(int, input().split())
    k = math.factorial(b) // (math.factorial(a) * math.factorial(b-a))
    print(k)



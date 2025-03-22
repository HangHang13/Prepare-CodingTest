n=int(input())
x = int(input())
lst = list(map(int,input().split()))
if x>n:
    print(0)
    quit()

lst.sort()

k=[]
for a in range(1 ,n):
    k.append(lst[a]-lst[a-1])

k.sort()

for _ in range(x-1):
    k.pop()
print(sum(k))

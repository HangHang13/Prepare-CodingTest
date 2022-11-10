
n,m = map(int ,input().split())

lst1=[]

for _ in range(n+m):
    lst1.append(list(map(int, input().split())))


print(lst1)

lst1.sort(key=lambda x:(x[0],x[1]))

print(lst1)
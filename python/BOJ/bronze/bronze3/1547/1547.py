m=int(input())

lst=[0,1,0,0]
for _ in range(m):
    a,b = map(int, input().split())

    lst[a] ,lst[b] = lst[b], lst[a]


for a in range(0, len(lst)):
    if lst[a] == 1:
        print(a)
    else:
        pass

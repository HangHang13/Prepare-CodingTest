n,m = map(int, input().split())
lst = []
for a in range(n):
    lst.append([])
    lst[a].append(1)

    for j in range(1,a):
        lst[a].append(lst[a-1][j-1]+lst[a-1][j])

    if n!=0:
        lst[a].append(1)


print(lst[n-1][m-1])
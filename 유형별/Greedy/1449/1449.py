
n,l = map(int, input().split())

lst = list(map(int, input().split()))

# lst.sort(reverse=1)
lst.sort()


start = lst[0]

cnt=1

for i in lst[1:]:
    if i in range(start, start+l):
        continue
    else:
        start = i
        cnt+=1


print(cnt)

n=int(input())


lst = list(map(int, input().split()))




lst.sort(reverse=1)

cnt=1
for a in range(len(lst)-1):
    if lst[a] > lst[a+1]:
        cnt+=1
    else:
        continue



print(cnt)

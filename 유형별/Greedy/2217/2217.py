n=int(input())

lst = []
kk = [0]*n
for _ in range(n):
    lst.append(int(input()))


lst.sort(reverse=1)
for i in range(1,len(lst)+1):
    lst[i-1] = lst[i-1]*i

print(max(lst))
n, m =map(int, input().split())



kk = []
k = []

for _ in range(n):
    a=input()
    kk.append(a)

for _ in range(m):
    b=input()
    k.append(b)



cnt=0

for i in k:
    if i in kk:
        cnt+=1

print(cnt)
a = input().split('-')

cnt=0

for i in a[0].split('+'):
    cnt+=int(i)
for i in a[1:]:
    for j in i.split('+'):

        cnt-=int(j)


print(cnt)
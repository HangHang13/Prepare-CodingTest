b=int(input())
a=1000-b
k=[500,100,50,10,5,1]


cnt=0
for ab in k:
    cnt+=a//ab
    a=a%ab


print(cnt)



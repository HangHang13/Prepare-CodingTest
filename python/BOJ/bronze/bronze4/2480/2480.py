

lst = list(map(int,input().split()))

cnt=0
if lst[0]==lst[1] and lst[1]==lst[2]:
    cnt+=10000+lst[0]*1000
elif lst[0]==lst[1] and lst[1]!=lst[2]:
    cnt+=1000+lst[0]*100
elif lst[0]!=lst[1] and lst[1]==lst[2]:
    cnt+=1000+lst[1]*100
elif lst[0]!=lst[1] and lst[0]==lst[2]:
    cnt+=1000+lst[0]*100
else:
    cnt+=max(lst)*100

print(cnt)
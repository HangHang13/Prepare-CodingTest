

n= int(input())

lst=[]
for _ in range(n):
    a = int(input())
    lst.append(a)
cnt=0

card = lst[1:n]
da = lst[0]

if len(lst) ==1:
    print(0)
else:
    while 1:
        card.sort(reverse=True)
        if card[0]<da:
            print(cnt)
            break
        else:
            card[0]-=1
            da+=1
            cnt+=1

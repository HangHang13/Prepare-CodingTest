n=int(input())



cnt=0
for _ in range(n):
    a = input()

    lst=[]
    for i in a:
        if i not in lst:
            lst.append(i)
        else:
            if lst[-1]==i:
                lst.append(i)
            else:
                lst=[]
                break
    if lst:
        cnt+=1


print(cnt)
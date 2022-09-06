n=int(input())
cnt=0
cos1=[]
cos2=[]
cos3=[]
while 1:
    cos1.append(n)
    if n%3==0:
        cnt +=1
        n=n//3

    elif n%2==0:
        cnt+=1
        n=n//2
    else:
        n = n - 1
        if n<2:
            break
        else:
            cnt += 1


    print(n)

print(cnt)
print(cos1)
while 1:
    a = input()
    if a =='0' :
        break

    ans=2+len(a)-1
    for i in range(len(a)):
        if a[i] =='1':
            ans+=2
        elif a[i] == '0':
            ans+=4
        else:
            ans+=3

    print(ans)



n,m = map(int, input().split())




cnt=1

while 1:
    if m==n:
        break
    elif (m%2 != 0 and m%10 !=1) or (m<n):
        cnt = -1
        break
    else:
        if m%10 ==1:
            m//=10
            cnt+=1
        else:
            m//=2
            cnt+=1

print(cnt)

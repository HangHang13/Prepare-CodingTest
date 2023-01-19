tc = int(input())


for i in range(tc):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))


    lst = [0 for i in range(n)]
    lst[m] = 1
    cnt=0
    while 1:
        if q[0] == max(q):
            cnt+=1
            if lst[0] != 1:
                del q[0]
                del lst[0]
            else:
                print(cnt)
                break
        else:
            q.append(q.pop(0))
            lst.append(lst.pop(0))






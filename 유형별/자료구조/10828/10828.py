
n=int(input())
import collections
q= collections.deque()


for _ in range(n):
    q.append(input())
con=[]
while q:
    cont = q.popleft()
    if 'push' in cont:
        conn=cont.split(" ")
        con.append(conn[-1])
    elif cont == 'top':
        if len(con)==0:
            print(-1)
        else:
            print(con[-1])
    elif cont =='size':
        print(len(con))
    elif cont =='empty':
        if len(con)==0:
            print(1)
        else:
            print(0)
    elif cont == 'pop':
        if con:
            a=con.pop()
            print(a)
        else:
            print(-1)






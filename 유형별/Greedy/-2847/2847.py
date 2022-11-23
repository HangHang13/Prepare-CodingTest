n=int(input())


cnt=0
ant=0

for _ in range(n):
    a=int(input())
    if a<=ant:
        while 1:
            ant-=1
            cnt+=1
            if ant<a:
                break
    ant = a

print(cnt)



n, m = map(int,input().split())

arr = [[0]* m for _ in range(m)]
x,y = 0,0
for _ in range(n):
    a,b = input().split()
    if a == 'MOVE':
        
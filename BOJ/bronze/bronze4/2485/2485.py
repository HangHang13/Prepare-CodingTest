import sys
input = sys.stdin.readline

a,b = map(int, input().split())
aa=[]
aa=list(map(int, input().split()))

c=a*b

for a in aa:
    print(a-c, end=" ")
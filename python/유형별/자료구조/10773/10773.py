import collections


# q= collections.deque()
q=[]
n=int(input())


for _ in range(n):
    a= int(input())
    if a==0:
        q.pop()
    else:
        q.append(a)

print(sum(q))
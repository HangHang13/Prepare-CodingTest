import sys
import collections
import itertools
sys.stdin = open('input.txt')


n =int(input())
q= []
for _ in range(n):
    q.append(input())

print(q)
k = {}

for a in q:
    cnt = len(a)
    for c in a:
        print(c)
        if c not in k:
            k[c]=(10**(cnt-1))
            print(k)
        else:
            k[c]+=(10**(cnt-1))
            print(k)
        cnt-=1

print(k)
khan = list(k.values())
khan.sort()
khan.reverse()
num = 9
ans=0
for i in khan:
    ans+=i*num
    num-=1
print(ans)
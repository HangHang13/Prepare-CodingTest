import sys
import collections
import itertools
sys.stdin = open('input.txt')


kk = ['a', 'e', 'i','o', 'u']
aa,b = map(int, input().split())

n =input().split()
n.sort()
arr=[]

#조합
# for a in itertools.combinations(n,aa):
#     arr.append(a)
arr = itertools.combinations(n,aa)
T=[]

for a in arr:
    t = ''
    for b in a:
        t+=b
    T.append(t)

for a in T:
    x=0
    y=0
    for i in range(aa):
        if a[i] in arr:
            x+=1
        else:
            y+=1
    if x>= 1 and y>=2:
        print(''.join(a))
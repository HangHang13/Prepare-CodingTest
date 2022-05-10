import sys
import collections
import itertools
sys.stdin = open('input.txt')


kk = ['a', 'e', 'i','o', 'u']
a,b = map(int, input().split())

n =input().split()
n.sort()
arr=[]

#조합
for a in itertools.combinations(n,4):
    arr.append(a)

T=[]

for a in arr:
    t = ''
    for b in a:
        t+=b
    T.append(t)
king = []
for a in T:
    for k in kk:
        if k in a:
            king.append(a)
khan = []
for k in king:
    if k not in khan:
        khan.append(k)
for a in khan:
    print(a)


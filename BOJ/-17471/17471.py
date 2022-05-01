import sys
import collections
import itertools
sys.stdin = open('input.txt')

t= int(input())
kk=collections.defaultdict()

for _ in range(1):
    n =int(input())
    lst = list(map(int, input().split()))
    ko=[]
    for a in range(1,n+1):
        ko.append(list(map(int, input().split())))
        for b in ko:
            kk[a]=b[1:]

    print(kk)
    k = [a for a in range(1,n+1)]
    aa = list(itertools.combinations(k,2))
    print(aa)
    tt=[]
    for a in range(1, n+1):
        tt.append(list(itertools.combinations(k,n-a)))


    print(tt)
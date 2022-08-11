import sys
input = sys.stdin.readline
import collections

q=collections.deque()
n= int(input())
for _ in range(n):
    kk=input().split()
    k=int(input())
    arr = input()
    t=list()
    for x in arr:
        if x =='[' or x==']' or x==',' or x =='\n':
            continue
        else:
            t.append(x)
    # print(t)
    if len(t) == 2 or len(t) == 0:
        print('error')
    else:
        while kk:
            ab = kk.pop(0)
            if ab=='R':
                t.reverse() #시간복잡도 높음
            elif ab=='D':
                t.pop(0)
    print(t)


import collections
import sys


word = sys.stdin.readline().rstrip()
check = collections.Counter(word)

cnt = 0
res = ''
mid = ''

for a,b in list(check.items()):
    if b % 2 ==1:
        cnt+=1
        mid = a
        if cnt >=2:
            print("I'm Sorry Hansoo")
            exit(0)



for a,b in sorted(check.items()):
    res += (a*(b//2))
print(res + mid + res[::-1])


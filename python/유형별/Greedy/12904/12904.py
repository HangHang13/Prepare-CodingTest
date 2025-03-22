import sys
import collections

q = collections.deque([])


s = list(input().rstrip())
t = list(input().rstrip())

#
# a = True
# while t:
#     if t[-1] == 'A':
#         t.pop()
#     elif t[-1] == 'B':
#         t.pop()
#         t.reverse()
#
#     if s==t:
#         a = False
#         break
#
# if not a:
#     print(1)
# else:
#     print(0)


print(s)
print(t)
q.append(s)
#
# while q:
#     q.popleft()
#     if len(s) != len(t):
#         q.append(s.append())
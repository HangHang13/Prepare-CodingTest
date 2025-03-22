import math

l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())

aa=math.ceil(a/c)
bb=math.ceil(b/d)
# if aa.isdemical():
#     pass
# else:
#     aa+=1
# if bb.isdemical():
#     pass
# else:
#     bb+=1
k = max(aa,bb)
print(l-k)
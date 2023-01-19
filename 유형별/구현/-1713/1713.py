n=int(input())
a=int(input())
import collections
lst= collections.deque([])
lst = list(map(int,input().split()))
pic = []
print(lst)
cha = [0]*a

while lst:
    t = lst.pop(0)
    cha[t-1]+=1
    pic.insert(0,t)
    if len(pic) >= n:
        aa = min(cha)
        _min_list = []
        for idx in range(len(cha)):
            if cha[idx] == aa:
                _min_list.append(cha[idx])
                if len(_min_list) > 3:
                    pic.pop()
                    break

    print(pic)





al =[0,0,1,1]

print(min(al))





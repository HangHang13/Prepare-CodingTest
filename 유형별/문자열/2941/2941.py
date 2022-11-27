


cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]


lst = input()



for i in cro:
    lst= lst.replace(i,"*")

print(len(lst))
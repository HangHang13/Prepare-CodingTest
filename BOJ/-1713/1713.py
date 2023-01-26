n=int(input())
a=int(input())
lst =list(map(int, input().split()))
com = [0]*(a)


while lst:
    stack = []
    num = lst.pop(0)
    com[num]+=1

    stack.append(num)

    if len(stack) >3:
        while len(stack) ==3:
            idx = com.index(min(com))
            stack.remove(idx)
            com[idx] = 0
print(stack)

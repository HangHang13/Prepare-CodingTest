ppap = input()
p = ['P', 'P','A','P']

if ppap == 'P' or ppap == 'PPAP':
    print('PPAP')
else:
    stack = []
    for i in ppap:
        stack.append(i)
        if stack[-4:] == p:
            stack.pop()
            stack.pop()
            stack.pop()


    if stack == ppap or stack ==['P']:
        print('PPAP')
    else:
        print('NP')

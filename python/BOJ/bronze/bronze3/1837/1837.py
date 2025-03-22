p,k = map(int, input().split())
bad_case = k

for i in range(2,k):
    if p % i ==0:
        if bad_case > i:
            bad_case =i
if bad_case != k:
    print('BAD', bad_case)
else:
    print('GOOD')

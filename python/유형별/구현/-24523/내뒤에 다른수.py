
n = int(input())
lst = list(map(int, input().split()))


arr = [-1]*n

for i in range(n):
    _max = 100000000000
    for j in range(i+1, n):
        if lst[j]!=lst[i]:
            if lst[j]<_max:
                _max = lst[j]
    if _max == 100000000000:
        _max=lst.index(lst[i])
    _idx = lst.index(_max)
    arr[_idx] = _max
print(*lst)
print(arr)
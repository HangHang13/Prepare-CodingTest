import sys

from queue import PriorityQueue

# input = sys.stdin.readline
sys.stdin = open("input.txt", "rt")

n = int(input())
q = PriorityQueue(maxsize=n)
arr = []
_max = 0
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

    q.put((a, b))

_max = max(arr, key=lambda x: x[1])[1]
arr.sort(key=lambda x: (x[0], x[-1]))
print(arr)

cnt = 0

vis = [False] * (n + 1)


def get_index(a, arr):
    ans = 0
    for x, y in arr:
        ans += 1
        if y == a:
            return ans - 1
        else:
            continue


for i in range(len(arr)):
    print(arr[i][1])
    if arr[i][1] >= _max:
        cnt += arr[i][1]
    else:
        cnt += _max
        idx = get_index(_max, arr)
        arr.pop(idx)
        _max = max(arr, key=lambda x: x[1])[1]

print(cnt)

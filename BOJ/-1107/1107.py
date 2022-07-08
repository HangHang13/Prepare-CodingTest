# 백준 1107
# 브루트포스 리모컨

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

button = list(map(int, input().split()))

cnt = abs(100 - n)

for i in range(1000001):
    tmp = list(str(i))
    flag = False
    # 숫자중에 못누르는 버튼이 있으면 통과
    for j in tmp:
        if int(j) in button:
            flag = True
            break
    if flag:
        continue
    # 가장 가까운 버튼 중에서 n-i 한 값 + 길이(가장 가까운 위치만큼 리모콘 누르기때문)
    else:
        cnt = min(cnt, abs(n - i) + len(str(i)))

print(cnt)

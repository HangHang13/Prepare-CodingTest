import sys
sys.stdin = open('sample_input.txt')

#swea에서 본 답
def func(x):
    l = len(x)
    res = 0
    visited = [1] * l
    queue = [[visited, sum(x)]]
    while queue:
        tmp = queue.pop(0)
        tmp_sum = tmp[1]
        tmp = tmp[0]

        if tmp_sum <= c:
            tmp_squre = 0
            for i in range(l):
                if tmp[i] == 1:
                    tmp_squre += x[i] ** 2
            if res < tmp_squre:
                res = tmp_squre
        else:
            for i in range(l):
                if tmp[i] == 1:
                    tmp[i] = 0  ## 여기서 tmp가 계속 같은거 사용해서 그럼 ㅠ

                    queue.append([tmp[:], tmp_sum - x[i]])
                    tmp[i] = 1

    return res


t = int(input())

for case in range(t):
    n, m, c = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    sum_lst = [[0] * (n - m + 1) for _ in range(n)]
    for i in range(n):
        for j in range(n - m + 1):
            tmp1 = lst[i][j:j + m]
            sum_lst[i][j] = func(tmp1)

    tmp = [0] * n
    for i in range(n):
        tmp[i] = max(sum_lst[i])
    tmp = sorted(tmp, reverse=True)
    res = sum(tmp[:2])
    for i in range(n):
        for j in range(n - m + 1 - m):
            tmp = sum_lst[i][j]
            for k in range(n - m + 1 - m - j):
                tmp += sum_lst[i][j + m + k]
                if res < tmp:
                    res = tmp
                tmp -= sum_lst[i][j + m + k]

    print(f'#{case + 1} {res}')
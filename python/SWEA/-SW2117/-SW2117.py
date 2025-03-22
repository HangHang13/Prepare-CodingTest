import sys
sys.stdin = open('sample_input.txt')

#swea에서 본 답

T = int(input())

for a in range(1):
    N, M = map(int,input().split())

    home = []
    for a in range(N):
        home.append(list(map(int,input().split())))


    act = []
    for a in range(N):
        for b in range(N):
            if home[a][b]==1:
                act.append((a,b))


    res=1
    for k in range(2, N + 2):
        for a in range(N):
            for b in range(N):
                cnt=0
                for y,x in act:
                    if abs(a-y) + abs(b-x) < k:
                        cnt+=1
                if cnt > res and cnt * M >= k ** 2 + (k - 1) ** 2:
                    res = cnt


    print(act)










'''
T = int(input())
for test_case in range(1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    houses = []  # 집 리스트
    for r in range(N):
        for c in range(N):
            if MAP[r][c]==1:
                houses.append((r, c))
    print(houses)
    result = 1  # K가 1일때 결과
    for K in range(2, N + 2):
        for r in range(N):
            for c in range(N):
                # 범위 안의 집 세기
                cnt = 0
                for y, x in houses:
                    if abs(r - y) + abs(c - x) < K:
                        cnt += 1
                # 손해 안나면서 많은 집이 가능할 경우 갱신
                if cnt > result and cnt * M >= K ** 2 + (K - 1) ** 2:
                    result = cnt

    print('#{} {}'.format(test_case, result))

'''


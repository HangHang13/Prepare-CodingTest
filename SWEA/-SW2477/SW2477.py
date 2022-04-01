import sys
import collections
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n, m, k, a, b = map(int,input().split())  # 정비소에는 N개의 접수 창구와 M개의 정비 창구, 정비소를 방문한 고객 K, 지갑을 두고 간 고객이 이용한 창구의 번호 (접수, 정비)
    a_time = list(map(int, input().split()))  # 접수하는데 걸리는 시간
    b_time = list(map(int, input().split()))  # 정비하는데 걸리는 시간
    t = list(map(int, input().split()))  # 고객이 도착한 시간

    take = [0] * len(a_time)  # 접수한 시간
    fix = [0] * len(b_time)  # 정비한 시간
    use_a = []
    use_b = []
    take_wait = []
    fix_wait = []

    idx = 1

    cnt_done = 0
    cnt = 0
    while cnt_done<k:



        for i in range(len(t)):
            if t[i]<=cnt:
                take_wait.append(idx)
                t.pop(0)
                idx+=1

        for i in range(n):
            if take[i]==0 and take_wait:
                take[i].append([take_wait.pop(0),cnt])

        for i in range(m):
            if fix[i]==0 and fix_wait:
                fix[i].append([fix_wait.pop(0),cnt])
        cnt+=1
    result = 0
    for i in use_a:
        if i in use_b:
            result += i
    print("#%d %d" % (tc, result if result != 0 else - 1))

'''

    while cnt_done < k:
        for i in range(m):
            if fix[i] == 0:
                continue
            if cnt - fix[i][1] >= b_time[i]:
                if i == b - 1:
                    use_b.append(fix[i][0])
                cnt_done += 1
                fix[i] = 0

        for i in range(n):
            if take[i] == 0:
                continue
            if cnt - take[i][1] >= a_time[i]:
                if i == a - 1:
                    use_a.append(take[i][0])
                fix_wait.append(take[i][0])
                take[i] = 0

        for i in range(len(t)):
            if t[0] <= cnt:
                take_wait.append(idx)
                t.pop(0)
                idx += 1

        for i in range(n):
            if take[i] == 0 and take_wait:
                take[i] = [take_wait.pop(0), cnt]

        for i in range(m):
            if fix[i] == 0 and fix_wait:
                fix[i] = [fix_wait.pop(0), cnt]

        cnt += 1

'''
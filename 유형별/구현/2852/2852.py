import sys


input = sys.stdin.readline
n = int(input())
def timetominute(tm):
    hour, second = tm.split(":")
    return int(hour) * 60 + int(second)
def minutetotime(tm):
    a = tm//60
    b = tm%60
    return ''.join([str(a),':',str(b)])


team1 = 0
team2 = 0
win = 0
for tt in range(n):
    team,t = input().split()
    if team == '1':
        if win == 0:
            win = 1
        elif win == 2:
            team2 += timetominute(t)
    else:
        if win == 0:
            win = 2
        elif win == 1:
            team1 += timetominute(t)
    if tt == len(n)-1:


print(team1)
print(team2)
print(minutetotime(team1))
print(minutetotime(team2))





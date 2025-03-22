n = int(input())  ##사진틀 갯수
vote = int(input())  ## 총 추천 횟수
student = list(map(int, input().split()))  # 추천학생 번호
pic = []  # 사진틀
score = []  # 사진틀과 매치하여 추천수 저장할 리스트

for i in range((vote)):
    if student[i] in pic:
        for j in range(len(pic)):
            if student[i] == pic[j]:
                score[j] += 1
    else:
        if len(pic) >= n:
            for j in range(n):
                if score[j] == min(score):
                    del pic[j]
                    del score[j]
                    break

        pic.append(student[i])
        score.append(1)

pic.sort()
print(' '.join(map(str, pic)))

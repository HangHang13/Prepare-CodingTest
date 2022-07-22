# 모음의 개수 다국어한국어  

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 128 MB      | 6779 | 3878 | 3550      | 59.355%   |

## 문제

영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장이 주어진다. 각 줄은 최대 255글자로 이루어져 있다.

입력의 끝에는 한 줄에 '#' 한 글자만이 주어진다.

## 출력

각 줄마다 모음의 개수를 세서 출력한다.

## 예제 입력 1 복사

```
How are you today?
Quite well, thank you, how about yourself?
I live at number twenty four.
#
```

## 예제 출력 1 복사

```
7
14
9
```



## 풀이

```python
import sys
sys.stdin = open('input.txt')


lst = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
k=[]
kk=[]
while 1:
    n=input()
    if n == '#':
        break
    k=[]
    for a in range(0,len(n)):
        k.append(n[a])

    cnt = 0
    for a in k:
        if a in lst:
            cnt += 1
        else:
            continue

    print(cnt)


```


# 집 주소 다국어한국어  

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 128 MB      | 3792 | 2732 | 2527      | 74.214%   |

## 문제

재석이는 대문에 붙이는 (주소를 나타내는) 호수판 제작업체의 직원이다. 고객에게 전달할 호수판은 숫자와 숫자 사이 그리고 왼쪽 오른쪽으로 적당히 여백이 들어가 줘야하고 숫자마다 차지하는 간격이 조금씩 상이하다. 다행이도 규칙은 매우 간단하다. 

1. 각 숫자 사이에는 1cm의 여백이 들어가야한다.
2. 1은 2cm의 너비를 차지해야한다. 0은 4cm의 너비를 차지해야한다. 나머지 숫자는 모두 3cm의 너비를 차지한다.
3. 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.

![120.png](https://upload.acmicpc.net/f203f2d5-ff6a-4afb-9cfe-226612dd4095/-/preview/)

예를 들어 위의 120 같은 경우, 각 숫자 사이에 여백이 1cm 씩 2개 들어간다. 1은 2cm, 2는 3cm, 0은 4cm를 차지한다. 오른쪽, 왼쪽 경계에서 각각 여백이 1cm씩 차지한다. 따라서 총 2 + 2 + 3 + 4 + 1 + 1 = 13(cm) 가 된다.

재석이는 고객에게 전달해야할 호수판의 너비가 얼마나 되는지 궁금해졌다. 재석이를 도와주자!

## 입력

호수판에 들어갈 숫자 N의 범위는 1 ≤ N ≤ 9999 이다.

입력은 마지막에 0이 들어오기 전까지 계속해서 줄 단위로 주어진다.

또한, 마지막의 0은 처리하지 않는다.

## 출력

각 입력마다 얼마만큼 너비를 차지하는지 정수로 출력하면 된다.

각 출력은 줄바꿈으로 구분되어야한다.

## 예제 입력 1 복사

```
120
5611
100
0
```

## 예제 출력 1 복사

```
13
15
14
```

## 풀이

```python
while 1:
    a = input()
    if a =='0' :
        break

    ans=2+len(a)-1
    for i in range(len(a)):
        if a[i] =='1':
            ans+=2
        elif a[i] == '0':
            ans+=4
        else:
            ans+=3

    print(ans)

```

- 숫자를 str 형태로 받고 탐색하는 형태로 구했다.
- EOF에러가 떴는데 찾아보니까 잘못된 입력 형식이 1개 이상일 때 발생한다고한다.
- 처음에 if a==0 으로 해서 적절히 끊지 못해서 생긴 문제인 것 같다.
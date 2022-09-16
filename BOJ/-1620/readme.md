## 입력

첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져. N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 뭔지는 알지? 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.

둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어. 아참! 일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야. 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!

## 출력

첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 말해줬으면 좋겠어!!!. 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력하면 돼. 그럼 땡큐~

![img](https://www.acmicpc.net/upload/201004/pn.PNG)

이게 오박사님이 나에게 새로 주시려고 하는 도감이야. 너무 가지고 싶다ㅠㅜ. 꼭 만점을 받아줬으면 좋겠어!! 파이팅!!!

## 예제 입력 1 복사

```
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
```



## 풀이

```python
import sys

input = sys.stdin.readline


n,m = map(int, input().split())


dict = {}

for i in range(1,n+1):
    a = input().rstrip()

    dict[i]=a
    dict[a]=i

print(dict)
# {1: 'Bulbasaur', 'Bulbasaur': 1, 2: 'Ivysaur', 'Ivysaur': 2, 3: 'Venusaur', 'Venusaur': 3, 4: 'Charmander',
#  'Charmander': 4, 5: 'Charmeleon', 'Charmeleon': 5, 6: 'Charizard', 'Charizard': 6, 7: 'Squirtle',
#  'Squirtle': 7, 8: 'Wartortle', 'Wartortle': 8, 9: 'Blastoise', 'Blastoise': 9, 10: 'Caterpie', 'Caterpie': 10, 11: 'Metapod', 'Metapod': 11, 12: 'Butterfree', 'Butterfree': 12, 13: 'Weedle', 'Weedle': 13, 14: 'Kakuna', 'Kakuna': 14, 15: 'Beedrill', 'Beedrill': 15, 16: 'Pidgey', 'Pidgey': 16, 17: 'Pidgeotto', 'Pidgeotto': 17, 18: 'Pidgeot', 'Pidgeot': 18, 19: 'Rattata', 'Rattata': 19, 20: 'Raticate', 'Raticate': 20, 21: 'Spearow', 'Spearow': 21, 22: 'Fearow', 'Fearow': 22, 23: 'Ekans', 'Ekans': 23, 24: 'Arbok', 'Arbok': 24, 25: 'Pikachu', 'Pikachu': 25, 26: 'Raichu', 'Raichu': 26}

for i in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(dict[int(a)])
    else:
        print(dict[a])
```


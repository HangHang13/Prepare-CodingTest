# πBOJ 14889 μ€ννΈ λ§ν¬

## πΊνμν κ°λ

- forλ¬Έ λ£¨νλ¬Έ νμ©
- μ‘°ν©
- itertools


## πΊνμ΄κ³Όμ 

- ν¬ν¬μΈν° νμ©? μμ΄λ κ°μ₯ λ§μ§λ§ μ°Έμ‘°ν  μ μλλ‘νκΈ°

## πΊμ½λ

```python
import itertools
#sys.stdin=open('input.txt')

#μλ ₯
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

    #nλ§νΌ νλ μ΄μ΄ μ«μλ§λ€κΈ°
player= [i for i in range(n)]

#print(f'player : {player}')
#player : [0, 1, 2, 3]


#nλ§νΌ νλ μ΄μ΄μ€, n//2λ§νΌ μ‘°ν©μΌλ‘ νμ λλ
team=[]
for a in itertools.combinations(player, n//2):
    team.append(list(a))
#print(f'team : {team}')
#team : [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]


ans=[]
#ν¬ν¬μΈν° νμ©? λ§¨μμ΄λ  λ§¨λ§μ§λ§ μ°Έμ‘°ν  μ μλλ‘νκΈ° μμ 1μ¦κ°μ λ€μ 1κ°μνλ μμΌλ‘
for t in range(len(team)//2):
    #μ΄κΈ°ν
    AA=0
    for y in team[t]:
        for x in team[t]:
            AA+=arr[y][x]
         
        	#0,0 1,1 2,2, 3,3 μ λͺ¨λ 0μ΄λ―λ‘ λν΄μ€λ μκ΄μμ
            #μ κ²½μ° AA+= arr[0][0]+arr[0][1]+arr[1][0]+arr[1][1]
            #AA+=arr[0][1]+arr[1][0]
            
    #μ΄κΈ°ν
    BB=0
    for y in team[-(t+1)]: 
        for x in team[-(t+1)]:
            BB+=arr[y][x]
            #μ κ²½μ° BB+= arr[2][3]+arr[2][2]+arr[3][2]+arr[3][3]
            #BB+=arr[2][3]+arr[3][2]
            
    ans.append(abs(BB-AA)) #tλ₯Ό μ€ννλ©΄μ κ·Έ μ΅μκ°λ€μ λ¦¬μ€νΈμ λν΄μ€
    
print(min(ans)) # tλ°λ³΅ν, κ°μ₯μμ κ° λμΆνκΈ°

```


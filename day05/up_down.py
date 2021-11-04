

import random
rn = random.randint(1,100) #1부터 100사이 난수 생성
num1 = 0
num2 = 0

print('[UP & DOWN 게임 - 1~100사이의 숫자 중 어떤 숫자가 들어있을까요???')    

while rn: #break가 나오기 전까지 계속 돌려라
     n = int(input('숫자를 입력하세요.(1 ~ 100)): '))
     print("입력값 = {}.format(n)")
    
while rn <= num2:
   
print(f'랜덤숫자: {rn}')


print('-'*40)

for n in random(1,100):
    print('숫자를 입력하세요(1 ~ 100): ')
    if n == x:
        print(("정답입니다!!"))

    if rn: break




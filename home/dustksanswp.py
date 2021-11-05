import random

print('~~~~~재미있는 사친연산 게임~~~~~')
print('[즐겁게 문제를 푸시다가 지겨우면 0을 누르세요~ ]')
print('='*40)

print('======#게임의 난이도를 선택하세요!! =======')
print('[1. 상 (1~100) | 2. 중 (1~50) | 3. 하 (1~20 ) ]')
level =int(input('>>>'))
if level == 1:
    levelnum = 100
elif level == 2:
    lebelnum = 50
elif level == 3:
    levelnum = 20
else:
    levelnnum = 999
Qnum = 1
ok = 0 #정답 횟수
no = 0 #틀린 횟수
while True:
    first = random.randint(1, levelnum)
    second = random.randint(1, levelnum)
    
    # 연산 기호를 결정할 랜덤숫자 생성
    marknum = random.randint(1,3)

    if marknum == 1:
        mark = '+'
        real = first + second
    elif marknum == 2:
        if first == second:
            second -= 1
        mark = '-'
        real = first - second
    else:
        mark = 'x'
        real = first * second

    print(f'\nQ{Qnum}. {first} {mark} {second} = ??')
       
    #사용자의 입력값
    answer = int(input('>> '))


    #종료조건 
    if answer ==0:
        print('게임을 종료합니다!!')
        print('----------------------------')
        print(f'정답횟수: {ok}회, 틀린횟수: {no}회')
        break

    if real == answer:
        print('정답입니다!!')
    else:
        print('틀렸습니다!!')
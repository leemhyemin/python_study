# 숫자 + 숫자 == ?? 
# >> 숫자
# 정답입니다!

import random
# answer = (number1) + (number2) 
print('~~~~~재미있는 사친연산 게임~~~~~')
print('[즐겁게 문제를 푸시다가 지겨우면 0을 누르세요~ ]')
print('='*40)

while True:
    number1 = random.randint(1,20)
    number2 = random.randint(1,20)
    print(f'\nQ1. {number1} + {number2} = ?? ')
    answer = int(input('>>'))
    if (number1) + (number2) == answer:
        print('정답입니다 ~!')
    elif (number1) + (number2) != answer:
        print('틀렸어요 ~!')
    else:
        print('0')
        print('게임을 종료합니다.')
        break

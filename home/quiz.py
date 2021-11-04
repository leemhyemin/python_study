# 랜덤 숫자 생성
# 숫자 입력받기
# 입력받은 숫자가 정답보다 큰지 작은지 판별
# 기회는 총 8번
#

print('[UP & DOWP 게임 !! 1부터 100 사이의 숫자 중 어떤 숫자가 들어있을까요???]')
rn = random.randint(1,100)
print(f'정답은 이거: {rn}')





import random

num1 = 0
num2 = 101

while rn < num1 :
    print('숫자를 입력하세요.(1 ~ 100)): ')
    num2 > rn
    if num1 == 0 :
         break 
    elif num1 > num2 :
         print('UP ! !')
    elif rn < num1 :
        print('DOUN ! !')
if rn == num1:
     print(f'\n 정답입니다!!.{num1}번만에 맞추셨군요~  YOU WIN!', {num2})
elif num1 == num2:
     print(f'\n 실패입니다. 정답 : , {rn}')
elif num <= num2:
     rint('정답 기회 모두 소진! 계속 문제를 풀어주세요!')
else:
     print(f'숫자 범위를 벗어났어요!!{rn}')

    




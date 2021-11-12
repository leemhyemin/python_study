# 랜덤 로또번호 만들기
import random

# 당첨번호
win_lotto = []

while len(win_lotto) < 6:
    rn = random.randint(1, 45) # 1~45 난수 생성
    if rn not in win_lotto:
        win_lotto.append(rn)

win_lotto.sort()
print('당첨번호:', win_lotto)

# 보너스 번호 생성
while True:
    bonus_x = random.randint(1, 45)
    if bonus_x not in win_lotto:
        bonus = bonus_x
        break

print(f'보너스 번호: {bonus}')

paper = 0
while True:

    # 내가 구매한 번호
    my_lotto = []

    while len(my_lotto) < 6:
        rn = random.randint(1, 45) # 1~45 난수 생성
        if rn not in my_lotto:
            my_lotto.append(rn)

    my_lotto.sort()
    paper += 1
    print('내 번호:', my_lotto)

    # ================================================

    count = 0 # 맞춘 개수를 저장

    for n in my_lotto:
        if n in win_lotto:
            count += 1    

    if count == 6:
        print('1등에 당첨되었습니다!')
        break
    else:
        print(f'로또 {paper}장째 구매중.....')        

print(f'맞춘 개수: {count}개')

# 등수 체크
if count == 6:
    count += 1 
    print('1등!')
    print('1500000000원')
elif count == 5:
    if bonus in my_lotto:
        count += 1 
        print('2등!')
        print('40000000원)
    else:
        count += 1 
        print('3등!')
        print('1000000원')
elif count == 4:
    count += 1 
    print('4등!')
    print('50000원')
elif count == 3:
    count += 1 
    print('5등!')
    print('5000원')
else:
    count += 1 
    print('꽝!')
    print('0원')

if len(my_lotto):
    print('======================================')
    print("당첨횟수, 당첨시 수령액(세후, 평균), 누적당첨금, 당첨확률, sep= ' '")


for m in count:

    count = my_lotto
    print(f'#{count}')
my_lotto.append(m)
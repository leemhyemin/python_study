
try:
    result = 10 / 0
except:
    print('0으로 나눌수 없습니다.')


while True:
    try: #예외 처리 
    # 예외 발생 가능성이 있는 코드
        n1 = int(input('정수1: '))
        n2 = int(input('정수2: '))
        print(f'입력한 정수: {n1}, {n2}')
        break

    except: #예외가 발생했을 경우 실행할 문장
        # 만약 예외가 발생하면 튕김을 방지하고 대체실행할 코드
        print('아,,,숫자로만 써')

# 예외 처리는 거의 필수! 


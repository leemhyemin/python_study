
# sale_rate = 0.8 # 전역 변수 전역적으로 쓸수 있는 변수

# def calc_price(price):
#     today_price = price * sale_rate
#     price(f'오늘의 가격: {today_price}원')

# print(sale_rate)
# print(today_price)  함수밖에서 x
# print(price)

# 전역 변수의 수정으로 인해 함수 실행결과가 바뀔 수 있다.
# 프로그램 만들때 전역 변수 많이 쓰지않기 별로 좋지않음.
# sale_rate = 0.6 

# calc_price(2000)

money = 1000 #전역 변수

def discount():
    # 함수를 통해 전역변수 값에 관여하려면 global 키워드를 사용
    global money # 앞으로 이 함수에서는 전역변수 money를 활용해라
    print('함수 discount 실행!')
    money = 500  # 지역 변수 
    # 함수 내부에서는 지역변수가 우선 !
    print(f'지역변수 money : {money}')
    print(f'지역변수 money의 메모리 주소값: {id(money)}')

discount()

print(f'전역변수 money: {money}')
print(f'지역변수 money의 메모리 주소값: {id(money)}')
#  주소가 다르다.
# global 쓰면 주소 같다



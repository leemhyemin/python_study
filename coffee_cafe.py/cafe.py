# ice hot
# print('# 회원가입') 리스트 이용해서 중복 확인
# print('# 로그인') ''

cafe_list = []
# 메뉴얼 함수
def manual():
    print('\n안녕하세요. 카페입니다.')
    print('# 1. 음료 등록')
    print('# 2. 디저트 등록')
    print('# 3. 음료 메뉴 조회')
    print('# 4. 디저트 메뉴 조회')
    print('# 5. 메뉴 수정하기')
    print('# 6. 메뉴 삭제하기')
    print('# 7. 프로그램 종료하기')

# 함수 정의부

#menu = input('카페 메뉴 입력: ')
#if menu =='1':
#coffee_name = input('음료 이름: ')
#if coffee_name not in coffee:
#price = input('음료 가격: ')


# 메뉴 - 음료 등록하는 함수
def coffee_list():
    menu = {}
    print('\n# 음료 메뉴 등록을 시작합니다.')

    menu ['음료'] = input('- 음료: ')
    menu ['가격'] = int(input('- 가격: '))
    cafe_list.append(menu)
    print('# 음료 등록이 완료되었습니다.')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')


# 메뉴 - 디저트 등록하는 함수
def dessert_list():
    dessert = {}
    print('\n# 디저트 메뉴 등록을 시작합니다.')

    dessert ['디저트'] = input('- 디저트: ')
    dessert ['가격'] = int(input('- 가격: '))
    cafe_list.append(dessert)
    print('# 디저트 등록이 완료되었습니다.')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')

# # 전체 메뉴 정보 출력 머리말 부분 함수
# def header_print():
#     print('=' * 55)
#     for coffee_name in cafe_list:
#         print('{:^8s}{:^8s}원'.format(coffee_name['음료명'], coffee_name['가격']))
#     print('=' * 55)

# 전체 음료 정보를 출력하는 함수
def print_all_coffee():
    print('\n\t****** 음료 메뉴판 ******')
    print('=' * 55)
    for menu in cafe_list:
        print('\t{:^8s}{:^8d}원'.format(menu['음료'], menu['가격']))
    print('=' * 55)

# 전체 디저트 정보를 출력하는 함수
def print_all_dessert():
    print('\n\t****** 디저트 메뉴판 ******')
    print('=' * 55)
    for dessert in cafe_list:
        print('\t{:^8s}{:^8d}원'.format(dessert['디저트'], dessert['가격']))
    print('=' * 55)


# 제품코드를 입력받는 함수
def input_code(msg):
    print(f'# {msg} 음료 이름을 입력하세요')
    code = input('=> ')
    return code

# 수정 삭제 하는 함수
def delete_cafelist():
        if len(foods) > 0:
            print('======메뉴판======')
            for c_coffee in cafe_list:
                c_dessert = cafe_list[c_coffee]
                print('# {:<3s}:{:>5d}원'.format(f_name, f_price))
            print('=======================')
            print('1.수정 |2. 삭제 |3.나가기')
            choice = int(input('>>> '))


# 프로그램 종료처리 함수
def exit_program():
    import sys
    print("# 프로그램을 종료합니다. [Y/N]")
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return



# 메인 실행부
if __name__ == '__main__':

    while True:
        manual()
        menu = int(input('=> '))

        if menu == 1:
            coffee_list()
            # 음료 메뉴얼
        
        elif menu == 2:
            dessert_list()
            # 디저트 메뉴얼

        elif menu == 3:
            print_all_coffee()
            # 음료 메뉴판

        elif menu == 4:
            print_all_dessert()
            # 디저트 메뉴판
        elif menu == 5:
            # 메뉴 음료수정
            pass
        elif menu == 6:
            # 메뉴 음료삭제
            pass
        elif menu == 7:
            # 메뉴 디저트 수정
            pass
        elif menu == 8:
            # 메뉴 디저트 삭제
            pass

        elif menu == 9:
            exit_program()
        else:
            print('# 메뉴를 잘못 입력했습니다.')

        input('#Enter를 누르시면 메뉴얼로 돌아갑니다.')









# 로그인 실패 횟수
cnt = 0
# Login System
while True:
 
    # ID, PW 입력받기
    id = input('ID 입력: ')
    pw = input('PW 입력: ')
 
    # ID 와 PW 일치하는지 비교
    if id=='superman' and pw=='1234':
        print('로그인 성공')
        break  
    else:
        cnt = cnt + 1
        print('로그인 {}회 실패'.format(cnt))
 
    if cnt >= 3:       
        print('보안을 위해 로그인 시스템을 종료합니다!')
        break
 
    #줄바꿈
    print()



info = {
    'way'.upper(): 'faith123'.upper(),
    'truth'.upper(): 'sight456'.upper(),
    'life'.upper(): 'living789'.upper()
    }
print('*****로그인*****')
uid = input('아이디: ').upper()
pwd = input('비밀번호: ').upper()
login = False
if uid in info.keys():
    if info.get(uid) == pwd:
        login = True
    else:
        print('비밀번호가 일치하지 않습니다.')
else:
    print('아이디가 일치하지 않습니다.')
msg = f'{uid}님, 환영합니다.' if login else '프로그램을 종료합니다.' # Ternary Operator: 3항 연산자
print(msg)
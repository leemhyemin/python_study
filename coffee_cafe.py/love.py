
# 1. 회원 정보 등록하기


# 4. 회원 정보 수정하기
# 5. 회원정보 삭제하기 remove
# 6. 프로그램 종료하기
# 메뉴입력:


# 전역변수
from sys import prefix


user = [
    {
    },
    {
    },
    {
    }
]


# 함수 정의부


# 메뉴를 출력하는 함수
def show_menu():
    print('\n***  회원가입 프로그램 ***')
    print('# 1. 회원가입 정보 등록하기')
    print('# 1. 회원 로그인하기')
    print('# 3. 회원 정보 수정하기')
    print('# 4. 회원 정보 삭제하기')
    print('# 6. 프로그램 종료하기')


# # 아이디 중복을 확인하는 함수
# def check_duplicate_code():    
#     while True:       
#         code = input(' - 아이디: ')    
#         flag = False  # 중복 플래그          
#         # 중복 검증
#         for p in user:
#             if code == p[' ']:
#                 # 중복됨
#                 print('# 아이디가 중복되었습니다. 다시 입력하세요!')   
#                 flag = True             
#                 break
#         if flag == False:
#             return code

# 회원 등록을 수행하는 함수
def insert_info():
    userinfo = {}
    print('\n# 제품 정보 등록을 시작합니다.')    
    
    userinfo['아이디'] = input('- 아이디: ')
    userinfo['비밀번호'] = input('- 비밀번호: ')
    userinfo['이름'] = input('- 이름: ')

    user.append(userinfo)
    print('#회원 등록이 정상처리되었습니다.')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')


# 프로그램 종료처리 함수
def exit_program():
    import sys
    print("# 프로그램을 종료합니다. [Y/N]")
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return



# 이름을 입력받아 아이디를 찾는 함수
def input_code(name):
    print(f'# {name}찾으실 이름를 입력하세요.')
    code = input('>> ')
    return code


# 제품번호로 해당 제품을 찾아오는 함수
def get_userinfo(code):
    for userinfo in user:
        if code == userinfo['아이디']:
            return userinfo
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴



# 개별 제품 조회 처리 함수
def search_product():
    code = input_code('조회')
    userinfo = get_userinfo(code)

    if len(product) > 0:
        header_print()
    else:
        print('# 존재하지 않는 아이디입니다.')


# 제품정보 수정 처리 함수
def modify_product():
    code = input_code('수정')
    userinfo = get_userinfo(code)
# 아이디 비번 수정 
    if len(userinfo) > 0:
        print('\n# [{}] {}의 정보를 수정합니다.'.format(userinfo['아이디'], userinfo['이름']))
        userinfo['제품명']
        print('[ 1. 아이디변경 | 2. 비밀번호 변경 | 3. 이름 변경 | 4. 취소 ]')
        select = int(input('>> '))
        
        if select ==1:
            # 딕셔너리 수정: 딕셔너리변수 [key] = new_value
            userinfo['수량'] = int(input('-수정할 수량({}): '.format(userinfo['수량'])))
        elif select ==2:
            product['가격'] = int(input('-수정할 가격({}): '.format(userinfo['가격'])))
            
        elif select ==3:
            userinfo['수량'] = int(input('-수정할 수량({}): '.format(userinfo['수량'])))
            userinfo['가격'] = int(input('-수정할 가격({}): '.format(userinfo['가격'])))
        else:
            print('# 변경을 취소합니다.')
    else:
        print('#존재하지 않는 아이디 입니다.')    
    
# 제품 정보 삭제 처리 함수
def delete_userinfo():
    code = input_code('삭제')
    userinfo = get_userinfo(code)

    if len(product) > 0:
        user.remove(userinfo)
        print('\n# 아이디가 정상 삭제 되었습니다.')
    else:
        print('# 존재하지 않는 아이디 제품입니다.')


# 메인 실행부
if __name__ == '__main__':
    

    while True:
        show_menu()
        menu = int(input('>> '))
        
        if menu == 1:
            insert_info()

        elif menu == 2:
            print_all_userinfo()

        elif menu ==3:
           search_userinfo()

        elif menu ==4:
            modify_userinfo()

        elif menu ==5:
            delete_userinfo()

        elif menu == 6:
            exit_program()
        else:
            print('# 메뉴를 잘못 입력했습니다.')

        input('#Enter를 누르시면 메뉴로 돌아갑니다.')



#  C R U D 



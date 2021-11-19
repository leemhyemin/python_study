from sys import prefix
# 회원가입
user = [
    {
        '이름': 'tom',
        '아이디' : 'abc123',
        '비밀번호': 'abcabc'
    }
]


# 함수 정의부
# 메뉴를 출력하는 함수
def show_menu():
    print('-' * 30)
    print('1 . 회원가입 ')
    print('2 . 로그인 ')
    print('3 . ID 찾기 ')
    print('4 . PW 찾기 ')
    print('5 . PW 바꾸기 ')
    print('6 . 회원 탈퇴 ')
    print('7 . 종료 ')


# ID와 PW을 등록하는 함수
def user_join():
    info = {}
    print('\n ☆ 회원 가입을 시작합니다. ☆')    

    info['이름'] = input(' 이름 : ')
    info['중복확인아이디'] = check_ID_code()
    info['아이디'] = input(' 아이디 : ')
    info['비밀번호'] = input(' 비밀번호: ')
    info['비밀번호'] = input(' 비밀번호 재확인: ')
    user.append(info)
    print('★ 가입을 축하합니다 ★')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')


# ID를 중복을 확인하는함수
def check_ID_code():    
    while True:       
        code = input(' 중복확인아이디: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in user:
            if code == p['중복확인아이디']:
                # 중복됨
                print('☞ 이미 사용중이거나 탈퇴한 ID 입니다 ☜')   
                flag = True             
                break
        if flag == False:
            return code


# {}을(를) 입력받는 함수
def input_code(msg):
    print(f'# {msg}를 위한 정보를 입력해주세요.')
    code = input('>> ')
    return code


# Id를 찾아오는 함수
def get_ID(code):
    for user in user_info:
        if code == user['회원아이디']:
            return user
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴


# 아이디 찾는 함수
def search_id():
    code = input_code('ID 찾기')
    ID = (code)

    if len(user) > 0:
        print(['아이디'])
    else:
        print(f'☞ 이미 사용중이거나 중복된 {user} 입니다 ☜')


# 프로그램 종료처리 함수
def exit_program():
    import sys
    print("# 가입을 종료합니다. [Y/N]")
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return


if __name__ == '__main__':

    # user_join()

    # while True:
        show_menu()
        menu = int(input('메뉴 입력 :  '))

        if menu == 1:
            user_join()
        elif menu == 2:
            pass
        elif menu == 3:
            get_ID()   
        elif menu == 4:
            pass
        elif menu == 5:
            pass
        elif menu == 6:
            pass            
        elif menu == 7:
            exit_program()
        else:
            print('# 메뉴를 잘못 입력했습니다.')

        input('#Enter를 누르시면 메뉴로 돌아갑니다.')
 














































# # 로그인
# info = {
#     }
# print('*****로그인*****')
# uid = input('아이디: ').upper()
# pwd = input('비밀번호: ').upper()
# login = False
# if uid in info.keys():
#     if info.get(uid) == pwd:
#         login = True
#     else:
#         print('비밀번호가 일치하지 않습니다.')
# else:
#     print('아이디가 일치하지 않습니다.')
# msg = f'{uid}님, 환영합니다.' if login else '프로그램을 종료합니다.' # Ternary Operator: 3항 연산자
# print(msg)



from sys import prefix
user = [
    {
        
    }
]

# 함수 정의부
# 메뉴를 출력하는 함수
def show_menu():
    print('\n 안녕하세요 ')
    print('#1 . 회원가입 ')
    print('#2 . 로그인 ')
    print('#3 . ID 찾기 ')
    print('#4 . PW 찾기 ')
    print('#5 . PW 바꾸기 ')
    print('#6 . 회원 탈퇴 ')
    print('#7 . 종료 ')

# 회원 등록하는 함수
def info_list():
    info = {}
    id1 = {}
    ps1 = {}
    print('\n# 회원 등록을 시작합니다.')

    info ['이름'] = input('- 이름: ')
    id1 = input('아이디를 입력해주세요(종료:q) : ')

    if id1 == 'q':
        return 'q'
    ps1 = input('비밀번호를 입력해주세요 : ')

    info ['비밀번호재확인'] = input('- 비밀번호재확인: ')
    user.append(info)
    user.append(id1)
    user.append(ps1)
    # 회원가입
    print('# 회원 등록이 완료되었습니다.')
    print('★ 가입을 축하합니다 ★')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')

def login():
    while True:
        print('========로그인========')
      
        id1=input('아이디를 입력해주세요 : ')

        ps2=input('비밀번호를 입력해주세요 : ')
        if id1 in len(user).keys():
            if user[id1] == ps2:
                print('로그인 되었습니다')
                break
      
        print('로그인 실패! 다시 로그인 해주세요')  


# def login():
#     while True:
#         print('========로그인========')
      
#         id2 = input('아이디를 입력해주세요 : ')
#         if id2 == user["아이디"]:
#             ps2 = input('비밀번호를 입력해주세요 : ')
#             if ps2 == user['비밀번호']:
#                 ps2 = input('로그인 성공하셨습니다.')
#                 break
#             else:
#                 print('비밀번호가 다릅니다.')
#         else:
#             print('아이디가 틀립니다 다시 입력하세요.')


        # if id2 in user:
        #     if(ps2 == user[id2]) :
        #         print('로그인 되었습니다')
        #         break
        #     elif user[id2] != ps2:
        #         print('비밀번호가 틀렸습니다')
        # else:
        #     print('없는 아이디 입니다 등록 먼저 해주세요')
            
        # print('로그인 실패! 다시 로그인 해주세요')


# 로그인
# def userinfo():
#     print('***** 로그인 해주세요 *****')
#     for n in user:
#         if n['아이디'] == input('아이디: ') and n['비밀번호'] == input('비밀번호: '):
#             print('로그인 되셨습니다.')
#         elif n['아이디'] == input('아이디: ') and n['비밀번호'] != input('비밀번호: '):
#             print('비밀번호 틀리셨습니다.')
#         else:
#             print('없는 계정입니다.')
#             break
#                 cnt = cnt + 1
#                 print('로그인 {}회 실패'.format(cnt))
#         if cnt >= 3:
#             print('아이디가 일치하지 않습니다.')
#             print('보안을 위해 로그인 시스템을 종료합니다!')
#             break
#         print(msg)
#         print()
# if len(user) > 0 :
    # cnt = 0
# 로그인
# def uwerinfo():
    
        
    # # id 와 pw 일치하는지 비교
    # login = False
    # while True:
    #     if uid in user.keys():
    #         if user.get(uid) == pwd:
    #             login = True
    #             print('로그인 되셨습니다.')
    #         else:
    #             cnt = cnt + 1
    #             print('비밀번호가 일치하지 않습니다.')
    #             print('로그인 {}회 실패'.format(cnt))
    #             break
    #     if cnt >= 3:
    #         print('아이디가 일치하지 않습니다.')
    #         print('보안을 위해 로그인 시스템을 종료합니다!')
    #         break
    #     msg = f'{uid}님, 환영합니다.' if login else '프로그램을 종료합니다.' # Ternary Operator: 3항 연산자
    #     print(msg)
        # print()



# # ID를 중복을 확인하는함수
# def check_ID_code():    
#     while True:       
#         code = input(' 아이디 : ')    
#         flag = False  # 중복 플래그          
#         # 중복 검증
#         for p in user:
#             if code == p['아이디']:
#                 # 중복됨
#                 print('☞ 이미 사용중이거나 탈퇴한 ID 입니다 ☜')   
#                 flag = True             
#                 break
#         if flag == False:
#             return code


# {}을(를) 입력받는 함수
def input_code(msg):
    print(f'# {msg}를 위한 정보를 입력해주세요.')
    code = input('>> ')
    return code


# Id를 찾아오는 함수
def get_ID(code):
    for user_info in user:
        if code == user_info['아이디']:
            return user_info 
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴


# 아이디 찾는 함수
def search_id():
    code = input_code('ID 찾기')
    user_info = get_ID(code)

    if len(user_info) > 0:
        print(['아이디'])
    else:
        print(f'☞ 이미 사용중이거나 중복된 {user} 입니다 ☜')


# 프로그램 종료처리 함수
# def exit_program():
#     import sys
#     print("# 가입을 종료합니다. [Y/N]")
#     answer = input('>> ')
#     if answer.lower()[0] == 'y':
#         sys.exit()
#     else:
#         return


if __name__ == '__main__':

    while True:
        show_menu()
        menu = int(input('메뉴 입력 : '))

        if menu == 1:
            info_list()
        elif menu == 2:
            login()
        elif menu == 3:
            get_ID()   
        elif menu == 4:
            pass
        elif menu == 5:
            pass
        elif menu == 6:
            pass            
        elif menu == 7:
            pass
            # exit_program()
        else:
            pass


from sys import prefix
# 회원가입
user = [
    {
    },
    {
    },
    {
    }
]
print(type(user))

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


def user_info():
    
    # name = input('- 이름: ')
    info = {}
    print('\n ☆\t회원 가입을 시작합니다. ☆')      
    info['이름'] = input('- 이름: ')
        
    while True:
        for info in user:
            id = input('- 아이디: ')
            if info['아이디'] == id :
                print('이미 등록된 아이디 입니다.')
                continue
            else:
                print('사용가능 아이디 입니다')
                pw1 = input('- 비밀번호: ')
                while True:
                    pw2 = input('- 비밀번호확인: ')
                    if pw1 == pw2 :
                        pw2 = info['비밀번호']
                        print('회원가입이 완료되었습니다.')
                        user.append(info)    
                        return
                    else:
                        print('비밀번호 확인이 틀렸습니다.')
                        continue
               

def login():
    print('----------로그인----------')
    print(user)
    while True: 
        for info in user:
            id = input('- 아이디: ')
            pw = input('- 비밀번호: ')
            if (info['아이디'] == id) and (info['비밀번호'] == pw):
                print('☆ 로그인 되셨습니다 ☆')
                print('{}님 환영합니다.'.format(info['이름']))
                return
            elif (info['아이디'] != id) and (info['비밀번호'] == pw):
                print('아이디가 틀렸습니다.')
            elif (info['아이디'] == id) and (info['비밀번호'] != pw):
                print('비밀번호가 틀렸습니다.')







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

    while True:
        show_menu()
        menu = int(input('메뉴 입력 :  '))

        if menu == 1:
            user_join()
        elif menu == 2:
            login()
        elif menu == 3:
            search_id()   
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
 











# # {}을(를) 입력받는 함수
# def input_code(msg):
#     print(f'# {msg}를 위한 정보를 입력해주세요.')
#     code = input('>> ')
#     return code


































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



import sys
# 회원가입 리스트 타입
user = []

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
# 회원가입
def user_info():
    info = {}
    print('\n ☆ 회원 가입을 시작합니다. ☆')      
    info['이름'] = input('- 이름: ')
    
    while True:
        for info in user:
            id = input(' - 아이디: ')
            if info['아이디'] == id :
                print('이미 등록된 아이디 입니다.')
                continue
            else:
                print('사용가능 아이디 입니다')
                info['비밀번호'] == input('- 비밀번호: ')
                while True:
                    pw = input(' - 비밀번호확인: ')
                    if info['비밀번호'] == pw:
                        print('회원가입 되셨습니다!')   
                        user.append(info)
                    else:
                        print('비밀번호가 일치하지 않습니다.')
                        continue
                    
                    

def login():
    print('----------로그인----------')
    while True:
        for info in user:
            id = input(' - 아이디: ')
            pw = input(' - 비밀번호: ')
            if (info['아이디'] == id) and (info['비밀번호'] == pw):
                print('☆ 로그인 되셨습니다 ☆')
                print('{}님 환영합니다.'.format(info['이름']))
                return
            elif (info['아이디'] != id) and (info['비밀번호' == pw]):
                print(' 아이디가 틀렸습니다.')       
            elif (info['아이디'] == id) and (info['비밀번호' != pw]):
                print(' 비밀번호가 틀렸습니다.')
            

# 프로그램 종료처리 함수
def exit_program():
    import sys
    print("# 프로그램을 종료합니다. [Y/N]")
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return

# 실행부
if __name__ == '__main__':
    while True: 
        show_menu()
        menu = int(input('메뉴 입력 = > '))
        if menu == 1:
            user_info()
        if menu == 2:
            login()
        if menu == 7:
            exit_program()
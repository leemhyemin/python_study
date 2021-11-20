# 회원가입 리스트 타입
info = {}

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
    print('\n ☆ 회원 가입을 시작합니다. ☆')
    user_name = input('- 이름: ')
    user_id = input('- 아이디: ')
    if user_id in [i[0] for i in info]:
        print('이미 등록된 아이디 입니다.')
        return
    else:
        print('등록되있지 않은 아이디 입니다')
    user_pw = input('- 비밀번호: ')
    if user_pw != input('- 비밀번호확인: '):
        print('비밀번호가 일치하지 않습니다.')
        return
    print('비밀번호가 일치하지 않습니다.')
    info[user_id] = (user_name,user_pw)
    print('회원가입 되셨습니다!')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')


def login():
    print('----------로그인----------')
    for n in user:
        while True:
            id = input('- 아이디: ')
            pw = input('- 비밀번호: ')
            if info.get(id, [None,None])[1] == pw:
                print('☆ 로그인 되셨습니다 ☆')
                break
            else:
                print('로그인 실패! 다시 로그인 해주세요.')

# 실행부
if __name__ == '__main__':
    while True:
        show_menu()
        menu = int(input('메뉴 입력 = > '))
        if menu == 1:
            user_info()
        if menu == 2:
            login()
            break
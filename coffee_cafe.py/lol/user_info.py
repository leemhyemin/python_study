
user = [
    {'이름': 'kgw',
    '별명': 'aaa',
    '아이디': 'aaaa',
    '비밀번호': '1111'},

    {'이름': 'kwj',
    '별명': 'bbb',
    '아이디': 'bbbb',
    '비밀번호': '2222'}


# Blank 회원가입 공백제거  함수
def user_info():
    info = {}
    print('\n☆ 회원 가입을 시작합니다. ☆')
    while True:
        name = input('이름: ')
        if len(name.strip()) == 0:
            print('아무것도 입력된게 없습니다.') 
        else:
            while True: 
                info['이름'] = name
                nickname = check_duplicate_nickname()
                if len(nickname.strip()) == 0:
                    print('아무것도 입력된게 없습니다. ')
                else:
                    while True:
                        info['별명'] = nickname
                        id = check_duplicate_id()
                        if len(id.strip()) == 0:
                            print('아무것도 입력된게 없습니다.')
                        else:
                            info['아이디'] = id
                            if info['아이디'] not in user:
                                print(' 사용가능 아이디 입니다')
                            else:
                                print('이미 등록된 아이디 입니다.')
                            while True:  
                                pw = input('비밀번호: ')
                                if len(pw.strip()) == 0:
                                    print('아무것도 입력된게 없습니다.')
                                else:
                                    info['비밀번호'] = pw
                                    pw2 = input('비밀번호 확인: ')
                                    if len(pw2.strip()) == 0:
                                        print('아무것도 입력된게 없습니다.')
                                    else:
                                        info['비밀번호'] == pw2   
                                        if info['비밀번호'] == pw2:
                                            user.append(info)
                                            print('회원가입 되셨습니다!')
                                            print('메뉴화면으로 돌아가시려면 Enter를 누르세요')
                                            input()
                                            return
                                        else:
                                            print('비밀번호가 일치하지 않습니다.')
                                            continue   

# 0 - 1_1 [회원가입] 함수 - 별명중복 
def check_duplicate_nickname():    
    while True:       
        info = input('- 별명: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in user:
            if info == p['별명']:
                # 중복됨 
                print('중복되었습니다 다시 입력하세요')
                flag = True             
                break
        if flag == False:
            return info

# 0 - 1_2 [회원가입] 함수 - 아이디중복 
def check_duplicate_id():    
    while True:       
        info = input('- 아이디: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in user:
            if info == p['아이디']:
                # 중복됨 
                print('중복되었습니다 다시 입력하세요')
                flag = True             
                break
        if flag == False:
            return info            
            
if __name__== '__main__':
    user_info()
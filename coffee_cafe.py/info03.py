# def menu_input():
#     print('*********************')
#     print('* 1. 회원가입       *')
#     print('* 2. 회원검색       *')
#     print('* 3. 회원탈퇴       *')
#     print('* 0. 종료           *')
#     print('*********************')
#     return int(input())

#입력
def meber_input():
    #아이디 입력

    mid=''
    while len(mid)<4:
        mid=input('ID: ')
        if mid in member:
            print('이미 존재하는 ID 입니다')
            mid=''
    #패스워드 입력        
    passw=''
    while len(passw)<6 or len(passw)>12 :
        passw=input('p/w: ')
    mem=[passw]
    # 이름,주소,전화,주민 이메일 입력
    for i in range(1,6):
        mm=input(hang[i]+': ')
        mem.append(mm)
    member[mid]=mem
print(meber_input())

#검색
def member_surch():
    print('=====<검색항목>======')
    print('= 1. ID             =')
    print('= 2. 이름           =')
    print('= 3. 이메일 주소    =')
    print('= 이외. 검색최소    =')
    print('=====================')
    ny = int(input())
    if ny==1:    # iD 검색이면 찾을 아이디에 입력분을 저장
        sid=input('찾을 id를 입력하세요.')
    else:
        if ny==2: 
            sp=1
        elif ny==3:
            sp=5
        else:
            return

        # id찾기가 아니면 해당 항목을 찾아  아이디에 찾은 아이디 저장
        sid=None
        smm=input('찾을 '+hang[sp]+'를 입력하세요.')
        for i in member:
            if member[i][sp]==smm:
                sid=i
                break

    if sid in member:
        print('ID: ',sid)
        for i in range(6):
            print(hang[i]+': '+member[sid][i])
    else:
        print('찾으시는 화원이 없습니다.')

#삭제
def member_del():
    did=input('삭제할 id를 입력하세요. ')
    if did in member:
        del member[did]
        print('ID: '+did,'가 삭제 되었슴니다.')
    else:
        print('찾으시는 화원이 없습니다.')

if __name__ == '__main__':

    while True:
        menu_input()
        menu = int(input('메뉴입력: '))

        if menu == 1:
            meber_input()
        if menu == 2:
            member_surch()
        if menu == 3:
            member_del()
            
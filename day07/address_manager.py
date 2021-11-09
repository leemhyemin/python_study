# 리스트를 이용한 연락처 관리 프로그램 
# 1. 연락처등록 이름저장 list 전화번호 list 리스트 2개 이용.
# 연락처 등록을 시작합니다. 이름: 전화번호: 님 연락처 저장완료!
# 2. 연락처검색
# 3. 연락처삭제
# 4. 모든연락처 조회
# 5. 프로그램종료
namelist = []
phonelist = []
while True:
    print('--------연락처 관리 프로그램--------')
    print('1. 연락처 등록')
    print('2. 연락처 검색')
    print('3. 연락처 삭제')
    print('4. 모든 연락처 조회')
    print('5. 프로그램 종료')
    print('------------------------------------')

    menu = input('메뉴입력: ')


    if menu == 1:

        print('-'*20)
        print('연락처 등록을 시작합니다.')
        name = input('이름: ')
        phone = input('전화번호: ')
        namelist.append
        phonelist.append

        print(f'{name}님 연락처 저장완료!')

    elif menu == 2:

        name = input('찾을 이름을 입력하세요: ')
        print('{name}님의 전화번호는 {phone}입니다.'.format)
    
    elif menu == 3:

        name = input('삭제할 이름을 입력하세요: ')
        namelist.remove(name)
        print('{name}님의 정보가 정상적으로 삭제되었습니다.'.format)
    
    elif menu == 4:

        print('========전체 연락처 조회========')

    elif menu ==5:
        
        print('프로그램 종료')

    else:
        break



# input('메뉴입력: ')
# print('연락처 등록을 시작합니다.')
# input('이름: ')
# input('전화번호: ')
# print('{}님 연락처 저장완료!')
# 2
# input('찾을 이름을 입력하세요:')
# print('{} 님의 전화번호는 {} 입니다.')
# 3
# input('삭제할 이름을 입력하세요: ')
# print('{}님의 정보가 정상적으로 삭제되었습니다.')
# 4
# print('========전체 연락처 조회========')
# list
# 5 break

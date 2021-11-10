# 리스트를 이용한 연락처 관리 프로그램 
# 1. 연락처등록 이름저장 list 전화번호 list 리스트 2개 이용.
# 연락처 등록을 시작합니다. 이름: 전화번호: 님 연락처 저장완료!
# 2. 연락처검색
# 3. 연락처삭제
# 4. 모든연락처 조회
# 5. 프로그램종료
namelist = [] #테스트 할땐 넣어두고 하기 
phonelist = []
while True:
    print('--------연락처 관리 프로그램--------')
    print('1. 연락처 등록')
    print('2. 연락처 검색')
    print('3. 연락처 삭제')
    print('4. 연락처 수정')
    print('5. 연락처 삭제')
    print('6. 모든 연락처 조회')
    print('7. 프로그램 초기화')
    print('------------------------------------')
    menu = int(input('메뉴입력: ')) 

    if menu == 1:
        print('-'*20)
        print('연락처 등록을 시작합니다.')
        name = input('이름: ')
        phone = input('전화번호: ')
        namelist.append(name)
        phonelist.append(phone)
        print(f'{name}님 연락처 저장완료!')

    elif menu == 2:
        name = input('찾을 이름을 입력하세요: ')
        if name in namelist:
            idx = namelist.index(name)
            print(f'{name}님의 전화번호는 {phonelist[idx]}입니다.')
        else:
            print(f'{name}님은 연락처 목록에 없습니다.')
    elif menu == 3:
        name = input('삭제할 이름을 입력하세요: ')
        if namelist in name:
            idx = namelist.index(name)
            del(namelist[idx])
            del(phonelist[idx])
            print(f'{name}님의 정보가 정상적으로 삭제되었습니다.')
        else:    
            print(f'{name}님은 연락처 목록에 없습니다.')
    elif menu == 4:
        find_name = input('찾을 이름을 입력하세요: ')
        if find_name in namelist:
            print(f'# {find_name}님의 연락처를 수정합니다.')
            idx = namelist.index(find_name)
            old_phone = phonelist[idx]
            phonelist[idx] = input('새로운 전화번호: ')
            print(f'{find_name}님의 전화번호가 {old_phone}에서 {phonelist[idx]}로 수정되었습니다.')    
        else:
            print(f'{name}님은 연락처 목록에 없습니다.')


    elif menu == 5:
        if len(namelist) > 0:
            print('========전체 연락처 조회========')   
            for idx in range(len(namelist)):
                print(f'# {idx+1}. {namelist[idx]} : {phonelist[idx]}')
        else:
            print('\n아직 등록된 데이터가 없습니다. 등록을 먼저 진행하세요!')
    elif menu == 6:        
        print('프로그램 종료')
        break
    elif menu == 7:
        print('프로그램 초기화')
        print('모든 데이터가 삭제됩니다. [y/n]') 
        answer = input('>> ')
        if answer.lower()[0] == 'y' or answer == 'ㅛ':
            namelist.clear()
            phonelist.clear()
            print('모든 데이터가 초기화되었습니다.') 
            

    else:
        print("메뉴를 다시 입력해주세요.")


            





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

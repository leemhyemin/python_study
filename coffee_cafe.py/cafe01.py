
id_list = [{

}]


# ID를 중복을 확인하는함수
def check_id_code():    
    while True:
        
        code = input('아이디: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in id_list:
            if code == p['아이디중복']:
                # 중복됨
                print('# 아이디가 중복되었습니다.!')   
                flag = True             
                break
        if flag == False:   
            return code


# # 회원가입 함수
def insert_product():
    product = {}
    print('\n# 회원 정보 등록을 시작합니다.')    
    
    product['아이디중복'] = check_id_code()
    product['아이디'] = input('ID : ')
    product['비밀번호'] = input('PW: ')
    id_list.append(product)
    print('#회원 등록이 정상처리되었습니다.')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')

# # 실행부
if __name__ == '__main__':
    insert_product()
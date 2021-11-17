# 1. 제품 정보 등록하기
# 2. 모든 제품 정보 조회
# 3. 개별 제품 정보 조회
# 4. 제품 정보 수정하기
# 5. 제품정보 삭제하기 remove
# 6. 프로그램 종료하기
# 메뉴입력:


# 전역변수
inventory = []
# 함수 정의부
def product_list():
    product = {}
    print('\n#제품 정보 등록을 시작합니다.')

    product['제품번호'] = input('- 제품번호: ')
    product['제품명'] = input('- 제품명: ')
    product['단가'] = int(input('- 단가: '))
    product['수량'] = int(input('- 수량: '))

    inventory.append(product)
    print('#제품 등록이 정상처리되었습니다.')
    print('메뉴화면으로 돌아가시려면 Enter를 누르세요')

# 메인 실행부
if __name__ == '__main__':
    

    while True:
        print('# 1. 제품 정보 등록하기')
        print('# 2. 모든 제품정보 조회')
        print('# 3. 개별 제품정보 조회')
        print('# 4. 제품정보 수정하기')
        print('# 5. 제품정보 삭제하기')
        print('# 6. 프로그램 종료하기')
        menu = int(input('# 메뉴 입력: '))
        
        if menu == 1:
            product_list()
        elif menu == 2:
            print(inventory)
        elif menu ==3:
            print('# 조회하실 제품의 번호를 입력하세요')
            menu = int(input('- 제품번호: '))
            print(len(inventory)[menu])
        elif menu ==4:
            print('수정하실 제품의 번호를 입력하세요.')
            product_list = int(input('- 제품번호: '))
            idx = inventory.index(product_list)
            new_product = product_list[idx]
            

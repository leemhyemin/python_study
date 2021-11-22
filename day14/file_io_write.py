

# 파일 저장 기능

# 내가 저장할 폴더 위치
dir_name = 'D:/isec_Hmo3o/py_study/'

# 저장할 파일명
file_name = input('파일명: ')

# 파일 저장 기능
text = '안뇽안녕 방가방가!! \n하하호호'

# 파일 저장할때는 예외처리 필수
try:
    # 파일 입출력을 실행하는 내장함수 open(path, mode)
    # path = 저장할 경로
    # mode 모드
    # w - 파일저장 | r - 파일로드
    f = open(dir_name + file_name + '.txt', 'w')

    f.write(text)
    print('파일저장 성공!')
except:
    print('파일 저장 실패!')
finally:
    f.close() #파일 입출력 할때 습관적으로 쓰기 ^메모리 자원반납^


'''
 사용자의 입력을 파일(xxx.txt)에 저장하는 프로그램을 작성하시오. 
(단, 프로그램을 다시 실행하더라도 파일명이 동일하다면
  기존 작성한 내용을 유지하고 
새로 입력한 내용이 추가되어야 한다. 또한 파일명도 입력받아 저장)

다음은 실행 예제이다.
출력 예시: "저장할 내용을 입력: "
실행 할 때마다 사용자가 입력한 내용이 xxx.txt파일에 추가되어야 한다.
'''
dir_name = 'D:/isec_Hmo3o/py_study/'
file_name = input('파일명: ')



print('저장할 내용을 입력("그만"이라고 입력시 종료됩니다)')
user_input = ""
while True:
    text = input()

    if text == '그만':
        print('종료합니다.')
        break
    user_input += text + "\n"


    try:
    # 파일 입출력을 실행하는 내장함수 open(path, mode)
    # path = 저장할 경로
    # mode 모드
    # w - 파일저장 | r - 파일로드
        f = open(dir_name + file_name + '.txt', 'w')

        f.write(text)
        print('파일저장 성공!')
        break

    except:
        print('파일 저장 실패!')
    finally:
        f.close() #파일 입출력 할때 습관적으로 쓰기 ^메모리 자원반납^

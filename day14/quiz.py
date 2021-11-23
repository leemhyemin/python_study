print("저장할 내용을 입력('그만'이라고 입력시 종료됩니다.) ")
user_input = ""
while True:
    temp = input()
    if temp == '그만': 
        break
    user_input += temp + "\n"
    
f_name = input("파일명을 입력: ")
f_path = "D:/isec_Hmo3o/py_study/{}.txt".format(f_name)
# encoding='UTF-8 한글 안깨지게 해주는것
# a는 파일은 냅두고 거기에 더 추가 저장
# a는 append개념 f_path open 개념
try:
    f = open(f_path, "a", encoding='UTF-8')  # 내용을 추가하기 위해서 'a'를 사용
    
    f.write(user_input)  # 입력된 내용을 줄단위로 구분하기 위해 줄바꿈 문자 삽입
    print("파일 저장 성공!")
except:
    print("파일 저장 실패!")
finally:
    f.close()
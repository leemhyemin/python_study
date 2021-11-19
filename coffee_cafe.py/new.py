
users = {}

def register():
  print('========회원가입========')
  id1 = input('아이디를 입력해주세요(종료:q) : ')

  if id1 == 'q':
    return 'q'
  ps1 = input('비밀번호를 입력해주세요 : ')
  users[id1] = ps1
  print('회원가입 되셨습니다!')
  

def login():
    while True:
      print('========로그인========')
      
      id2=input('아이디를 입력해주세요 : ')

      ps2=input('비밀번호를 입력해주세요 : ')
      if id2 in users.keys():
        if users[id2] == ps2:
          print('로그인 되었습니다')
          break
      
      print('로그인 실패! 다시 로그인 해주세요')  

while True:
  # 회원가입 모듈 호출
  if register() == 'q':    #반환값이 q 이면 프로그램 종료
    break

  yb = input('로그인 하시겠습니까? yes no : ')

  if yb.lower() == 'yes' :  # 입력값 소문자로 변환해서 비교
    login()
  else:
    yn = input('다시 회원가입 하시겠습니까? yes no : ')
    
    if yn == 'yes':
      continue
    else:
      break

print("프로그램 종료")
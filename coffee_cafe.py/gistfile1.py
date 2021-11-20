# coding: utf-8

'''
사용자로부터 아이디와 비밀번호를 입력받아 user_id 와 password를 매칭시켜본다.
만약에 유저가 있고, 패스워드가 맞으면 "Log In"을 출력한다.
그러나 유저가 없으면 "Not Found"를,
패스워드가 틀리면 "Wrong Password"를 출력한다.
'''

user_id = "studybee" # 아이디
password = "12345" # 비밀번호

# 사용자에게 값을 입력받아 위 변수와 비교하여 봅니다.
# 아래에 작성해보세요.

import sys


def main(uid, passwd):
    customer_info = {"studybee": "12345"}
    if customer_info.has_key(uid):
        if customer_info.get(uid) == passwd:
            print ("로그인")
        else:
            print ("비밀번호 틀림")
    else:
        print ("없는 아이디입니다")


if __name__ == '__main__':

    print(main())
    # if len(sys.argv) != 3:
    #     sys.exit("python this.py id passwd")
    # main(sys.argv[1], sys.argv[2])



user_id = ("studybee")
password = "12345"

input_id = raw_input("ID: ")
input_pw = raw_input("Password: ")

if (input_id == user_id and input_pw == password):
    print ("로그인")
elif (input_id != user_id ):
    print ("없는 회원입니다")
elif (input_id == user_id and input_pw != password):
    print ("비밀번호 틀림")
else:
    print ("Error: Check your input and try again.")

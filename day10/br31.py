


# 플레이어들의 이름을 저장할 리스트
print('### 베스킨 라빈스~~~ 써리 원~!')
print('- 참여인원을 입력(최소2 최대4')

player_list = [] #플레이어 닉네임
while True:
    player_num = int(input('>>> '))

    if player_num < 2 or player_num > 4:
        print('인원 범위가 알맞지 않음!(2 ~ 4 입력)')
        continue

    # 인원은 일단 제대로 썼음 player_num 인원
    print(f'\n{player_num}명의 플레이어가 참여했습니다')
    print('## 플레이어들의 닉네임을 등록합니다.')
    
    for i in range(player_num):
        while True:
            player_name = input(f'# {i+1}번 플레이어 이름: ')

            # 이름 검증
            # 1. 이름을 안적은 경우
            if len(player_name.strip()) == 0:
                print('# 필수 입력사항입니다.')
            # 2. 중복된 이름인 경우
            elif player_name in player_list:
                print('#이미 등록된 이름입니다.')
            # 3. 나쁜 이름인 경우
            elif player_name in ['또라이', '멍청이', '바보']:
                print('# 해당 이름은 사용할수 없습니다.')
            else:
                player_list.append(player_name)
                break

    turn = 0
    num = 0

while num < 31:
    print(f'# {player_list[turn%player_num]}의 턴!!!')
    print('[숫자를 입력하세요(최소 1개, 최대3개) | 예시:23 24 25]')
    print('# 마지막에 31을 입력하는 플레이어가 패배합니다.')
    print(f'# 현재 {num+1} 부터 입력하시면 됩니다!!')
    # num_input = True

    while num_input == True:
        num2 = input('>>> ')
        num2 = num2.split(" ")
        if num2[0] == "":
            print('!! 아무것도 입력안하면 안된다~~~')
        elif int(num2[0]) != num +1:
            print(f'숫자를 {num+1}부터 제대로 입력하세요!')
        elif len(num2) > 3:
            print('1개에서 3개 사이의 숫자를 입력하세요!')
        elif len(num2) == 2 and int(num2) + 1 != int(num2):
                print('순차적인 숫자를 입력하세요!!')

        else:
            num = int(num2[len(num2)-1])
            turn += 1
            
        
print(f"{player_list[turn%2]} 패배!!! 후훗 잔넨 (쑻) (쑻)")
print('###종료하시려면 Enter!!!!')

# 순차적인 숫자를 입력하세요!!
# 1개에서 3개 사이의 숫자를 입력하세요!
# 숫자를 1부터 제대로 입력하세요!
                                            
            # num = int(num2[len(num2)-1])
            # turn += 1

            # turn -= 1
       
        


    


nums = [1, 3, 5, 7]
print(nums)

# nums[4] = 9 (x)
nums.append(9) # append 뒤에 추가. 리스트 저장
print(nums)

nums.append('안녕')
print(nums)

nums.insert(2, 4) # 2 번 인덱스로 4를 삽입.
print(nums)

nums.insert(4, '메롱')
print(nums)

print('\n' *40)


# empty = [] 빈 리스트
# 배불러   break 
# 배불러 치기 전까지 무한대로 음식 입력
# 내가 먹고싶은 음식: [...]입력
print('='*40)
print('#먹고싶은 음식을 입력하세요~~')
print("[그만 입력하려면 '배불러' 라고 입력하세요.]")

food_list = []

while True:
    food = input('>') #반복 
    if food == '배불러':
        break
    # 음식 이름을 리스트에 저장 append 
    food_list.append(food_list)

print('입력을 종료합니다.')
print(f'내가 먹고 싶은 음식: {food_list}')




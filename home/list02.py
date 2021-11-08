


tvxq = ['영웅재중', '최강창민', '유노윤호', '믹키유천', '시아준수']

print(tvxq[2]) # 0, 1,*[2]*, 3, 4, 5, ....~
print(type(tvxq))
print(type(tvxq[0]))

print(tvxq[1].find('창')) #find 찾고싶은 문자,몇번 인덱스 ,몇번 인덱스
print(tvxq[1][3])
print(tvxq[3][:2]) 

# 리스트 슬라이싱
nums = [0,1,2,3,4,5,6,7,8,9] # range(10)

print(nums[2:5:1])
print(nums[:4])
print(nums[6:][1])

resuult = nums[5] + nums[2:7][3]
print(resuult)

print(type(nums[3]))
print(type(nums[2:5]))

print('='*40)

tvxq[2] = '아이노유노'
print(tvxq)

tvxq[4] = tvxq[0][:2]
print(tvxq)

s = 'hello'

s = s.replace('1', 'x', 1)
print(s)

print('='*40)

# import random

from random import randint, sample


rn = randint(1, 45)
print(f'rn: {rn}')

foods = ['짜장면', '볶음밥', '김치찌개', '샌드위치', '김밥']
selected = sample(foods, 2)
print(selected)

def mean(n1, n2):
    return (n1 + n2) / 2;
    
# as 뒤에 할 별칭
import statistics as st

# from statistics import mean, variance, stdev


print('='*40)

numbers = [35, 44, 99, 100, 33, 55, 66]
print('평균:', st.mean(numbers))
print('분산:', st.variance(numbers))
print('표준편차:', st.stdev(numbers))

# [파이썬 퀴즈5 - 반복문]


# 문제1)
# 단을 입력 받아서 구구단을 출력하세요. (for 사용)
# 입력 예) 7
# 출력 예) 7 * 1 = 7 ... 7 * 9 = 63

'''
dan = int(input("몇 단? : "))
for i in range(1, 10):  # 1 2 3  4 5 6 7 8 9
    print(f'{dan} x {i} = {dan*i} ')
    #print(dan, 'x', i, '=', (dan*i))
'''

# 문제2)
# 1 부터 입력한 수까지의 짝수 합과 홀수 합을 각각 출력하세요.

'''
num = int(input("숫자입력:"))

#1~입력한 숫자 반복
# 짝수? 홀수?   숫자%2 == 0 짝수 ,    != 0 홀수
even_sum = 0    #짝수합
odd_sum = 0     #홀수합
for i in range(1, num+1): #10  range(1, 11)
    #print(i, end =" ")
    if i%2 == 0: #짝수
        even_sum = even_sum + i
    else: # 홀수
        odd_sum = odd_sum + i

print('짝수합:', even_sum, " 홀수합:", odd_sum)
'''


# 문제3)
# x = [49, -17, 25, 102, 8, 62, 21]
# 리스트의 각 요소에 10을 곱한 값을 한 줄에 출력하세요.
'''
x = [49, -17, 25, 102, 8, 62, 21]
print(x)
#print(x*10)  10번 반복
for i in range(len(x)): # x 리스트의 인덱스를 0~반복
    print( x[i] * 10 , end=' ')
print()

for v in x:
    print(v*10, end=" ")
'''

# 문제4)
# 잔액 13000원 교통카드에서 1350원씩 차감하면서 잔액이 1350원 미만이 될 때까지
# '남은 잔액' 을 출력하세요. (while 사용)

money = 13000       #  1500 -> 1350 -> 150       1200       1350원 -> 0원

while money >= 1350:   # 1350>1350      850 >= 1350
    money = money - 1350
    print('잔액:', money)

print('-'*50)

money = 13000

while True:
    if money < 1350:
        break
    money = money - 1350
    print('잔액:', money)

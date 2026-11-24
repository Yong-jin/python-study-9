# 문제1)
# 사각형의 가로, 세로 길이를 한 줄에 공백으로 구분해서 입력 받고
# 넓이와 둘레를 아래처럼 출력하세요.
# 입력 예) 10 5
# 출력 예)
# 넓이 : 50
# 둘레 : 30

'''
width, height = map(int, input("가로 세로 입력 : ").split())
width, height = input("가로 세로 입력 : ").split()
print(width, height)
width = int(width)
height= int(height)
# 넓이 : 가로 * 세로
# 둘레 : 가로*2 + 세로*2     or  (가로+세로)*2
area = width * height   
perm = (width+height)*2
print("넓이 :" , area)
print("둘레 :" , perm)
'''

# 문제2)
# 국어, 영어, 수학 점수를 콤마로 구분해서 입력 받고
# 총점과 평균(소수점 둘째 자리까지)을 출력하세요.
# 입력 예) 90,85,77
# 출력 예) 총점 252, 평균 84.0

'''
kor, eng, math = map(int, input("국어 영어 수학 점수를 콤마로 구분해서 입력: ").split(','))
total = kor + eng + math
avg = total / 3

print("총점 ", total, ", 평균 ", avg)  #sep=''

print('총점 ', total, end=", ")
print("평균 ", avg)

print("평균 ", round(avg, 2) ) #반올림 round()

print(f'총점 {total}, 평균 {avg}')
print(f'총점 {total}, 평균 {round(avg, 2)}')
print(f'총점 {total}, 평균 {avg}')
print(f'총점 {total}, 평균 {avg:.2f}')
'''


# 문제3)
# 초(second)를 입력 받아서 '몇 시간 몇 분 몇 초' 로 출력하세요.
# 입력 예) 3725
# 출력 예) 1시간 2분 5초

# 1초   1분=60초    5분=300초    1시간=60*60=3600
# 3725 초 ->  1시간  125초    ->   120초 2분 -> 1시간 2분  5초
# 나누기 / //   나머지 %

'''
inp = int(input("초를 입력:"))
#print(int(inp/3600))
#print((inp//3600))

# hour = inp//3600
# minute = (inp%3600)//60
# second = (inp%3600)%60

hour = inp//3600
inp = inp%3600
minute = inp//60
inp = inp%60
second = inp

print(hour)
print(minute)
print(second)

print(f'{hour}시간 {minute}분 {second}초')
'''

# 문제4)
# 년, 월, 일을 입력 받아서 sep 을 사용해 2026/11/02 형태로 출력하세요.

#input("년,월,일 입력 : ").split(',')
year, month, day = input("년 월 일 입력 : ").split()

print(year, month, day, sep="/")  #2026/5/5   2026/05/05

print(year, month.zfill(2), day.zfill(4), sep="/")  #2026/5/5   2026/05/05

print(f'{year}/{month:0>5}/{day:0>2}')

#int() 숫자형태로
#{day:02d}



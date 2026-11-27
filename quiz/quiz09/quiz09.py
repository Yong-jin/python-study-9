# [파이썬 퀴즈9 - 2차원 리스트]


# scores = [
#     ['김철수', 90, 85, 77],
#     ['이영희', 72, 95, 88],
#     ['박민수', 65, 70, 92],
#     ['최지우', 98, 89, 94],
# ]
# (이름, 국어, 영어, 수학)


scores = [
    ['김철수', 90, 85, 77],
    ['이영희', 72, 95, 88],
    ['박민수', 65, 70, 92],
    ['최지우', 98, 89, 94],
]

# 문제1)
# 학생별 총점과 평균을 출력하세요.
# 출력 예) 김철수 총점 252 평균 84.0

for row in scores:
    #print(row)
    #print(row[0], row[1], row[2], row[3])
    #total = row[1] + row[2] + row[3]    #총점
    total = sum(row[1:])  # sum([90, 85, 77])
    avg = total / 3                     #평균
    print(row[0], "총점:", total, " 평균:", avg)

for name, kor, eng, math in scores:
    total = kor + eng + math
    #name 총점 평균 avg

# 문제2)
# 과목별(국어, 영어, 수학) 평균을 출력하세요.
kor_total = 0
eng_total = 0
math_total = 0
for row in scores:
    kor_total += row[1]
    eng_total += row[2]
    math_total += row[3]

print("국어 평균" , kor_total/len(scores) )
print("영어 평균" , eng_total/len(scores) )
print("수학 평균" , math_total/len(scores) )


# 문제3)
# 총점이 가장 높은 학생의 이름을 출력하세요.

largest = 0
largest_name = ''

for row in scores:
    total = sum(row[1:])  #점수만 더하기
    if total >= largest:
        largest = total
        largest_name = row[0]  #이름 
        #idx

print("제일 높은 총점:", largest, " 1등:", largest_name)

# row[idx][0] 이름이 1등


totals = [sum(row[1:])  for row in scores]
print(totals)

max_total = max(totals)
idx_max_total = totals.index(max_total)

print(scores[idx_max_total][0], "1등인 사람")


result = sorted(scores, key=lambda s: sum(s[1:4]), reverse=True)
print(result)
print("1등이름:" , result[0][0])

best_student = max(scores, key=lambda student: sum(student[1:]))
# ['최지우', 98, 89, 94]
print("1등이름:", best_student[0])


# 문제4)
# 3행 4열 2차원 리스트를 만들고 아래처럼 1부터 순서대로 채워서 출력하세요.
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

table = []
num = 1

for i in range(3):
    row = []
    for j in range(4):
        row.append(num)
        num += 1
    table.append(row)

print(table)

table = []

for i in range(3):
    row = []
    for j in range(4):
        row.append( i*4 + (j+1) )
    table.append(row)

print(table)

table2 = [ [ i*4 + (j+1)  for j in range(4) ]  for i in range(3) ]
print(table2)

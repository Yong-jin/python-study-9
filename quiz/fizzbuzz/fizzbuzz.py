

# FizzBuzz 문제
# 1 ~ 100 까지 출력하면서
# 3의 배수는 Fizz, 5의 배수는 Buzz, 3과 5의 공배수는 FizzBuzz 출력

# num%3 == 0   num%5 == 0       
# num%3 == 0  and  num%5 == 0       
# num%15 == 0


for i in range(1, 101):

    #if i%3==0 and i%5 ==0 :
    if i%15 == 0 :
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)

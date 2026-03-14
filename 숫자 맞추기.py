# 202503134 컴퓨터 공학과 김서현
import random

# 1부터 100 사이 랜덤 숫자 생성
secret_number = random.randint(1, 100)

print("숫자 맞추기 게임!")
print("1부터 100 사이 숫자를 맞춰보세요.")

while True:
    guess = int(input("숫자를 입력하세요: "))

    if guess < secret_number:
        print("너무 작습니다!")
    elif guess > secret_number:
        print("너무 큽니다!")
    else:
        print("정답입니다!")
        break

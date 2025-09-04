user_input = int(input("숫자를 입력해주세요: "))

for i in range(1, user_input + 1):
  if i % 2 == 1:
    print(i, end = ' ')
  else:
    continue

# 입력값 : 10
# 결과
# 1 3 5 7 9
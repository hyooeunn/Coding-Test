n = int(input("숫자를 입력해주세요: "))

for i in range(1, n + 1):
  if i % 2 == 0:
    continue
  print(i)

# 입력값 : 10
# 결과
# 1
# 3
# 5
# 7
# 9
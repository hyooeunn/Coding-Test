import sys

n = int(sys.stdin.readline())
numbers = []

for i in range(n):
    numbers.append(int(sys.stdin.readline()))
    
numbers.sort()

for j in numbers:

    print(j)

# sys.stdin.readline : input()과 비슷하게 사용자가 입력한 한 줄을 읽어오는 함수

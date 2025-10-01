n = int(input())
li = []

for _ in range(n):
    age, name = input().split()
    li.append([int(age), name])
    
li.sort(key = lambda x : int(x[0]))

for i in li:

    print(i[0], i[1])

# lambda : 함수 만드는 키워드 (이름 없는 간단한 함수)
# x → 정렬할 때, li 안의 각 원소 [age, name]이 하나씩 들어옴
# x[0] → 그 원소의 첫 번째 값(age)
# int(x[0]) → 그 값을 정수로 변환

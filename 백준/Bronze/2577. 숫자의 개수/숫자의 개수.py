a = int(input())
b = int(input())
c = int(input())

result = a * b * c
result_str = str(result)

for i in range(10):

    print(result_str.count(str(i)))

# count() : 특정 값이 몇번 등장했는 지 세어줌

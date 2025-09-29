n = int(input())

words = []
for i in range(n):
    words.append(input())
    
words = list(set(words))
    
words.sort()
words.sort(key = len)

for j in words:

    print(j)

# 변수명.sort() : 안의 값들을 오름차순으로 정렬

# key 매개 변수
# - sort()에는 key라는 옵션 존재
# key는 정렬 기준을 바꿔줌

# len : 문자열의 길이 반환
# *길이가 짧은 순서대로 정렬하려고 씀

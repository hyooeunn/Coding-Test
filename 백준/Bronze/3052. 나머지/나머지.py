arr = []

for i in range(10):
    num = int(input())
    arr.append(num % 42)

print(len(set(arr)))

# append : 리스트에 값 넣을 때 사용
# len : 몇 개 들어있는지 개수 세는 함수
# set : 리스트에서 중복 없애고, 몇 개인지 셀 때 자주 같이 사용

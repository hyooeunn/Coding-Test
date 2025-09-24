# 슬라이싱
while True:
    n = input().strip()
    
    if n == '0':
        break
    elif n == n[::-1]:
        print('yes')
    else:

        print('no')

# strip() : 양쪽 공백을 제거해주는 매서드
# n[::-1] : n을 뒤집은 문자열을 의미한다.

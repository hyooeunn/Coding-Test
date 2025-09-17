while True:
    t = list(map(int, input().split()))
    if t[0] == 0 and t[1] == 0 and t[2] == 0:
        break
        
    t.sort() # 제일 큰 변을 맨 뒤로 보내주는 것
    if t[0] ** 2 + t[1] ** 2 == t[2] ** 2:
        print('right')
    else:

        print('wrong')

# sort() : 작은 것부터 큰 것 순서대로 정렬 

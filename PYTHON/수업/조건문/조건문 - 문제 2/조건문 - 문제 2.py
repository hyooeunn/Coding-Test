id = 'hyoeun'
pw = '0817'

if id == 'hyoeun' and pw == '0817':
  print('로그인 성공')
elif id != 'hyoeun' and pw == '0817':
  print('아이디가 틀렸습니다')
elif pw != '0817' and id == 'hyoeun':
  print('비밀번호가 틀렸습니다')
else:
  print('로그인 실패')
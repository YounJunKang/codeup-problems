grade, clas, no = input().split()

print(grade, clas, sep='', end='')

if int(no) >= 10:
  print(no)
else:
  print('0'+no)
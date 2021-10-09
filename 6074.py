c = ord(input())
t = ord('a')
while t <= c:
    if t == c:
        print(chr(t),end ='')
    else: 
        print(chr(t),end =' ')
    t += 1 # t = t+1 / t+= 1
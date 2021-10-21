a, b = input().split()
a2 = ord(a)
b2 = ord(b)
b2 = b2+1

for c in range(a2, b2):
    c = chr(c)
    print(c, end=" ")



#1. 문자를 하나 입력 받는다.
#2. 문자를 숫자로 바꾼다. 
#3. 바꾼 숫자에 +1을 한다. 
#4. 이걸 다시 문자로 바꾼다.
#5. 출력 한다.

#c = input()
#n = ord(c)
#n = n + 1
#c = chr(n)
#print(c)
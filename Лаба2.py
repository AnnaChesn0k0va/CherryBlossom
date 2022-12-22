a= True
b= False
print(a and b)
print((a and b) or b)
print((a and b) or not (a and b))
print(a and b or not (a or b) or b)
print(b and b or not a and (a or b or a) or not (a or b))
print(1 >> 2)
print(1 & 0 | 1 >> 1)
print(1 & 0 | 1 >> 0)
print(0b101 & 0b111 ^ 0b111 | 0b010)

a= int(input())
b= int(input())
if a>b:
    print(b)
else:
    print(a)

a= int(input())
b= int(input())
c= int(input())
if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
elif c > b and c > a:
    print(c)
else:
    print(a)

a= int(input())
b= int(input())
c= int(input())
i = 0
if a!=b and a!=c:
    i=i+1
if b!=a and b!=c:
    i=i+1
if c!=a and c!=b:
    i=i+1
print(i)
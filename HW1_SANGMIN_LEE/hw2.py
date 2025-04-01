a = 'My name is Sangmin Lee'

print(len(a))
for i in range(0,10):
    print(a)

print(a[0])
print(a[0:4])
print(a[-4:])

b = ""
for i in range(0, len(a)):
    b += a[-i-1]
print(b)

print(a[1:len(a)-1])

print(a.upper())
print(a.lower())
print(a.replace('a', 'e'))
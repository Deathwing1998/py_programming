x = input('Load x = ')
y = input('Load y = ')
x = int(x)
y = int(y)
I = 0
for x in range(x, y + 1):
    if not x % 5:
        I += x

print(x)        

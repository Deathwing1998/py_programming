x = int(input('x '))
y = int(input('y '))
m = 0

for i in range(x,y + 1):
    if not i % 5:
        m += i
print(m)

x = int(input('x: '))
y = int(input('y: '))
s = 0

for num in range(x, y + 1):
    if not num % 5:
        s += num

print(s)

k = input("your colomn: ")
num = int(input("num? "))
t = []

for mod in k:
    if "0" <= mod <= "9":
        t.append(mod)

print(t)
print(t[num - 1])
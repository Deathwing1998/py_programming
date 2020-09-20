s = input()
summa = []

while s:
    summa.append(s)
    s = input()

summa = sorted(summa, reverse=True)
print("".join(summa))
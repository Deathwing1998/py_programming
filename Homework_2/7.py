from random import randint
rand = randint(0, 100)
image = int(input('Load = '))
while image != rand:
    if image > rand:
        print("Chislo less than yours")
    else:
        print("Chislo bigger than yours")
    umage = int(input('Load = '))
print("Congratulations!You found it")

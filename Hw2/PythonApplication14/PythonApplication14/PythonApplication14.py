from random import randint
dude = randint(0,100)
answ = int(input("enter your numb: "))

while answ != dude:
    if answ < dude:
        print("Numbes is bigger than yours")
    else:
        print("Number less than yours")
    answ = int(input("enter your numb: "))
print("Yeah,ur right,congrats")#возьми с полки пирожок

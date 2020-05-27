x = float(input('x = '))
y = float(input('y = '))

if x > 0 and y > 0:
    print('1st chetvert')
elif x < 0 and y < 0:
    print('3rd chetvert')
elif x < 0 and y > 0:
    print('2nd chetvert')
elif x > 0 and y < 0:
    print('4th chetvert')
elif not x or not y;
    print('tochka lezhit na osi')

def brackets(f):
    otkr = f.count('(')
    zakr = f.count(')')
    if otkr > zakr
        return 'nedostatochno ' + str( otkr - zakr ) + "zakr_brackets"
    elif otkr < zakr:
        return 'nedostatochno ' + str( zakr - otkr ) + "otkr_brackets"
    return "Normal"


Imagine = input('Load = ')
decision = brackets(Imagine)
print(decision)

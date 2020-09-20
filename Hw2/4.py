def skobki(a):
    cls_s = a.count(')')
    opn_s = a.count('(')
    if opn_s > cls_s:
        return 'Не хватает закрывающих скобок: ', opn_s - cls_s
    elif opn_s < cls_s:
        return 'Не хватает открывающих скобок: ', cls_s - opn_s
    return 'Всех скобок хватает'

print(skobki(input('example: ')))

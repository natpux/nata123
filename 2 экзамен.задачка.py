1. Напишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры. Остальные цифры должны заменяться звездочками
#2.  Напишите осмысленный декоратор.

#def karta(q):
#    def decorate(fn):
#        def karta_kredit(x,y,z,x1,y1,z1,x2,y2,z2):
#            print(q*'*')
#            result = fn(x,y,z,x1,y1,z1,x2,y2,z2)
#            print(result)
#            print(q*'*')
#            return result
#        return karta_kredit
#    return decorate
#@karta(25)
#def vvod(x,y,z,x1,y1,z1,x2,y2,z2):
#    return ('******',z1,x2,y2,z2)
#vvod(1,2,5,6,4,5,6,8,7)
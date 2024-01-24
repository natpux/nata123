#Задание №1,2
#1. Напишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры. Остальные цифры должны заменяться звездочками
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
# 1. Напишите функцию, которая будет принимать номер кредитной карты
# и показывать только последние 4 цифры. Остальные цифры должны заменяться звездочками

#def safe_number(number):
#    return (len(number) - 4) * '*' + number[-4:]


#creditcard_number = input('введите номер кредитной карты: ')

#if len(creditcard_number) < 4:
#    print('номер кредитной карты должен содержать не менее 4х цифр')
#else:
#    print(safe_number(creditcard_number))


#Задание №3 Реализовать на свободную темы все концепции ООП, соединенные единым смыслом.

#class Gruppa_222:

#    def _init_(self,age,gorod,profesia):
#        self.age:int =age
#        self.gorod:str =gorod
#        self.profesia:str =profesia
#        print("я учу python")


#    @classmethod
#    def OOP(cls):
#        print("Изучаю информацию по ООП")

#    def UK(cls):
#        print("Пытаюсь понять декораторы")

#    def UK1(cls):
#        print("Впитываю n-e количество новых терминов")

# дочерий класс личные данные(метод Наследования)
#class NataP(Gruppa_222):

#    def __init__(self,):
#        print("Я Наташа! Тише едешь дальше будешь!")
#        super().UK()  # (метод Наследования)

#    def OOP2(self):
#        print("Люблю готовить")
#        super().UK1()

#class PachaP(Gruppa_222):

#    def __init__(self, ):
#        super().UK()  # (метод Наследования)
#        print("Я.Паша!Всегда готов!")

#    def OOP2(self):
#        print("Люблю писать код")
#        super().UK1()
#Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным).
# Инкапсуляция делает некоторые из компонент доступными только внутри класса.
#    def _private(self):
#        print("Никогда не расскажу секрет крестиков-ноликов!")


#(ПОЛИМОРФИЗМ)возможность обработки разных типов данных, т. е. принадлежащих к разным классам, с помощью "одной и той же" функции, или метода
#Natacha=NataP()
#Natacha.OOP2()
#Natacha.OOP()
#Pavel=PachaP()
#Pavel.OOP2()
#Pavel._private()

#print("что делает перед экзаменом VladM?")

#VladM=Gruppa_222()
#VladM.OOP()

#print("что будет делать летом VladU ?")
#VladU=Gruppa_222()
#VladU.UK()

#print("что делает после экзамена Artem?")
#Artem=Gruppa_222()
#Artem.UK1()


#4.   Дан класс корзина продуктов. реализовать сложение и вычитание из продуктов.
# В качестве корзины предусмотреть словарь, в который будут помещены продукты
# Создаете 2 разных объекта, они должны складывать, вычитать.
#**Так же реализуйте бонусную систему.

class Korzina_Productov:
    def __init__(self, products:dict, bonus):
        self.bonus = bonus
        self.products = products

    def summa(self):
        print( f"{sum(self.products.values())}-{self.bonus}")
        print(f"{sum(self.products.values())-self.bonus}")



Korzina1=Korzina_Productov({"помидоры": 3,"огурцы": 2},2).summa()
Korzina2=Korzina_Productov({"шоколад": 5,"мармелад": 2},1).summa()





























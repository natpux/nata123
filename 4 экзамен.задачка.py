# Дан класс корзина продуктов. реализовать сложение и вычитание из продуктов.
# В качестве корзины предусмотреть словарь, в который будут помещены продукты
# Создаете 2 разных объекта, они должны складывать, вычитать.
#**Так же реализуйте бонусную систему.


class Korzina_Productov:
    def __init__(self, products1:dict,n:int):
        self.products1= products1
        self.n=n

    def __add__(self, other):
        print(f"Метод  _add_update, обьединяет 2 корзины  {self.products1.update(other.products1)}")

    def summa(self):
         print(f"{sum(self.products1.values())}шт. сложение количества продуктов в корзине №{self.n}")

    def bonus(self):
        bonus=0
        if sum(self.products1.values())<=20:
            bonus+=20
        else:
            20<sum(self.products1.values())<50
            bonus +=50
        print(f"Количество бонусов для корзины № {self.n} равно {bonus}")



    def dob_product(self, new_product,kol):  # добавление нового продукта в корзину
        New_korzina=self.products1
        for key in self.products1.items():
            if key in self.products1:
                New_korzina[new_product]+=kol
            else:
                New_korzina[new_product] = kol
            return New_korzina



    def star_product(self,star_product,kol):  # добавление существующего продукта в корзину
        New_korzina=self.products1
        print( f"Так выглядит корзина перед добавление существующего продукта{New_korzina}")
        print(f"добавляем продукт {star_product} в количестве {kol} шт")
        for key in New_korzina.items():
            if key in New_korzina.items():
                New_korzina[star_product]=New_korzina.get(star_product,0)+kol
                return f"Теперь одинаковых продуктов в корзине с учетом сложения {New_korzina}"


    def pop_product(self,star_product,kol):  # исключение существующего продукта в корзину
        such_korzina1=self.products1
        print( f"Так выглядит корзина перед исключением существующего продукта{such_korzina1}")
        print(f"исключили продукт {star_product} в количестве {kol} шт")
        for key in such_korzina1.items():
            if key in such_korzina1.items():
                such_korzina1[star_product]=such_korzina1.get(star_product,0)-kol
                return f"Теперь одинаковых продуктов в корзине с учетом исключения продукта {such_korzina1}"


a=Korzina_Productov({"селедка":6,"яблоко":6,"арбуз":30},1)
b=Korzina_Productov({"арбуз":2,"яблоко":6,"водка":5},2)
a.summa()
b.summa()
b.bonus()
a.bonus()


a.__add__(b)
print(a.products1)


с=a.dob_product("гранат",10)
print(f"Добавили новый продукт(гранат) в корзину {с}")


z=b.star_product("яблоко",100)
print(f"Добавили продукт,который есть в корзине  {z}")


s=b.star_product("водка",20)
print(f"Добавили продукт,который есть в корзине  {s}")


s=b.star_product("водка",20)
print(f"Добавили продукт,который есть в корзине  {s}")

t=b.pop_product("водка",33)
print(t)







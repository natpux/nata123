4.#   Дан класс корзина продуктов. реализовать сложение и вычитание из продуктов.
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






class Car:
    def __init__(self, c, b, m, f):
        self.__color = c
        self.__brand = b
        self.__model = m
        self.__fuel = f

    def show(self):
        print(self.__color, self.__brand,
              self.__model, self.__fuel)


car1 = Car('Green', 'Ford', 'Mustang', 'Gasoline')
car2 = Car('Red', 'Toyota', 'Prius', 'Electricity')
car3 = Car('Blue', 'Volkswagen', 'Golf', 'Diesel')

car1.show()
car2.show()
car3.show()
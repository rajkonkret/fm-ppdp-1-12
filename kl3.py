class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # zmienna prywatna

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10

    def __zmien_bieg(self):
        print("Zmiana biegu")


car1 = Car("Opel Insgnia", 2017)
print(car1)  # <__main__.Car object at 0x000001E0BBBCCBE0>
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# po oznaczeniu jako zmienna prywatna
# AttributeError: 'Car' object has no attribute '__predkosc'.
# Did you mean: '_Car__predkosc'?
# print(car1.__predkosc)
car1.licznik()
car1.__predkosc = 0
car1.licznik()
# Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()

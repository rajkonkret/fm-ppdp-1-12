from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kokokokoko")

    def dziobanie(self):
        print(f"Tu {self.gatunek}, idę sobie podziobać")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print('kier kiir')

    def poluj(self):
        print(f"Tu {self.gatunek}, rozpoczynam polowanie")


# Po oznaczeniu jako klasa abstrakcyjna
# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos
# or1 = Ptak("Orzeł", 45)
# or1.latam()
# ku1 = Ptak("Kura", 0)
# ku1.latam()

ku2 = Kura("Kura")
ku2.latam()
ku2.wydaj_odglos()
ku2.dziobanie()

or2 = Orzel("Orzel", 45)
or2.wydaj_odglos()
or2.latam()
or2.poluj()

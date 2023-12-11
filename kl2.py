class Human:
    """
    Klaa opisujaca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca - konstruktor
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """

        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def moj_wiek(self):
        print("Wiek", self.wiek)

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem")
        else:
            print("Ruszyłam")


cz1 = Human("Anna", "45", 168)
cz1.powitanie()
print(cz1.plec)
print(cz1.wiek)
print(cz1.wzrost)

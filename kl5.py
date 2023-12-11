class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedsatw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manago(Pracownik):  # dziedziczenie po Pracownik
    """
    Menago
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.premia + self.pensja


pracownik = Pracownik("Jan", "Kowalski", 4249)
pracownik.przedsatw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f'wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: {wyn_prac} zł')

manago = Manago("Anna", "Nowak", 8000, 3000)
manago.przedsatw_sie()
wyn_men = manago.oblicz_pensje()
print(f'wynagrodzenie dla pracownika {manago.imie} {manago.nazwisko}: {wyn_men} zł')

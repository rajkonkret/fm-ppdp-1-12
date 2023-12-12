# klasy -

class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam sie {self.imie}")


ob = Human()
print(ob.__doc__)
print(print.__doc__)
print(ob.plec)
print(ob.wiek)
print(ob.imie)

ob.imie = "Radek"
print(ob.imie)
print(type(ob))

cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = "40"
cz2.plec = "m"
cz2.powitanie()

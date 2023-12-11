# funkcje zwracające wynik
def dodaj(a, b):
    return a + b  # zwraca wynik


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


dodaj(7, 8)
print(dodaj(5, 6))  # 11
print(odejmij())
print(odejmij(1))
print(odejmij(1, 2))
print(odejmij(b=8, a=7))

print(oblicz_vat(1000))
print(oblicz_vat(1000, 23))
print(oblicz_vat(vat=8, cena=5000))
# print(odejmij(b=9, c=8, 2))  # SyntaxError: positional argument follows keyword argument
print(odejmij(1, b=6, c=8))

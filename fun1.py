# funkcja - wydzielony fragment kodu, ktory mozna uzyc wielokrotnie
a = 8
b = 9


# deklaracja funkcji
def dodaj():
    c = 7  # zmienna lokalna
    print(a + b)


def dodaj2(a, b):  # obowiązkowo muszą byc przekazane parametry
    print(a + b)


# można zasymulowac przciązanie argumentów funkcji
# poprzez wartość domyślną
def odejmij(a, b, c=0):  # c - parametr domyślny
    print(a - b - c)


dodaj()  # 17
dodaj2(5, 6)
odejmij(1, 2)
odejmij(1, 2, 3)  # argumenty pozycyjne
odejmij(b=7, c=7, a=9)  # argumenty prekazana po nazwie
# print(dodaj())  # None
# TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'
# print(odejmij(1, 2) - odejmij(5, 7))

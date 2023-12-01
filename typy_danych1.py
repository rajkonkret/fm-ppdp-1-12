wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float
wiek2 = 37, 5
print((type(wiek2)))  # <class 'tuple'> krotka

print(wiek)
print(type(wiek))  # <class 'int'>
print(type(temp))  # <class 'float'>

print(6 * "Radek")  # RadekRadekRadekRadekRadekRadek
print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023232822540781017
# float
print(wiek // rok)  # 0 czesc całkowita
print(wiek % rok)  # reszta z dzielenia czyli modulo
print(5 % 2)  # 1 bp 2 całe i reszta 1
print(wiek ** rok)  # potęgowanie

print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - (5 * 43) + (4 / 2 + 4) / 2)
print(2 ^ 3)  # XOR bitowo
print(0.2 + 0.8)  # 1.0
print(0.1 + 0.5)
print(0.1 + 0.2)  # 0.30000000000000004
print(0.2 + 0.7)  # 0.8999999999999999
# float ma bład zaokrąglenia
print(f"{0.2 + 0.7:.1f}")  # 0.9
print(f"Sprawdenie zmiennej {temp} {wiek}")
print(f"""
{temp}
    {wiek}""")

# typ logiczny
# True, False
czy_znasz_python = True
print(czy_znasz_python)  # True
print(int(czy_znasz_python))  # 1
print(int(False))  # 0
print(bool(1))  # True
print(bool(100))  # True
x = -10
print(bool(x))  # True
print(bool(""))  # False
x = None
print(bool(x))  # False

# and - i
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# True
# False
# False
# False

# or lub
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# True
# True
# True
# False

# negacja not
print(not True)
print(not False)

x = 1
print(not x == 1)
print("-----")
print(None is None)  # True
print(None == None)  # True Comparison with None performed with equality operators

a = 8
b = 7

print(f"Porównanie {a} > {b}", a > b)
print(f"Porównanie {a} < {b}", a < b)
print(f"Porównanie {a} == {b}", a == b)  # równe
print(f"Porównanie {a} >= {b}", a >= b)
print(f"Porównanie {a} <= {b}", a <= b)
print(f"Porównanie {a} != {b}", a != b)  # rózne

# Porównanie 8 > 7 True  ##
# Porównanie 8 < 7 False
# Porównanie 8 == 7 False
# Porównanie 8 >= 7 True
# Porównanie 8 <= 7 False
# Porównanie 8!= 7 True

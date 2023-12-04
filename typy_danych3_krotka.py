# krotka - sekwencja niezmienna
# jednoelementowa krotka wypełnia znamiona zmiennej

tupla = "radek"
print(type(tupla))  # <class 'str'>
tupl2 = ("Raadek")
print(type(tupl2))  # <class 'str'>
tupl3 = ("Raadek",)
print(type(tupl3))  # <class 'tuple'>
temp = 36, 6  # to jest tupla(krotka)
print(type(temp))  # <class 'tuple'>
print(temp)  # (36, 6)

tuple_names = "Radek", "Tomek", "Zenek", "Bartek"
tuple_names2 = ("Radek", "Tomek", "Zenek", "Bartek")
print(type(tuple_names))  # <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# są immutable
# temp[0] = 1  # TypeError: 'tuple' object does not support item assignment
# del temp[0]  # TypeError: 'tuple' object doesn't support item deletion
del temp  # usunięcie całej tupli z pamięci

print(tupla_liczby[0])
print(tupla_liczby[1:3])
print(tupla_liczby[:3])
print(tupla_liczby[0:3])
print(tupla_liczby[2:])
# 43
# (55, 22.34)
# (43, 55, 22.34)
# (43, 55, 22.34)
# (22.34, 11, 200)
# wypisanie ostatniego elemntu
print(tupla_liczby[-1])
# odwrócenie tupli i wpisanie do nowej
print(tupla_liczby[-1::-1])  # -1, koniec,krok=-1 do tyłu
# (200, 11, 22.34, 55, 43)
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(tupla_liczby[:])  # wypisanie całej tupli

print(tuple_names)
# ('Radek', 'Tomek', 'Zenek', 'Bartek')
print("Radek" in tuple_names)  # True

# count() - policzy ilosc wystąpień
print(tuple_names.count("Tomek"))

# index() - sprawdzenie indexu dla elemntu
print(tuple_names.index("Radek"))

# sorted() - sortowanie sekwencji, zwroci posortowaną listę
print(sorted(tuple_names))
# ['Bartek', 'Radek', 'Tomek', 'Zenek']
print(sorted(tuple_names, reverse=True))  # ['Zenek', 'Tomek', 'Radek', 'Bartek']

# rozpakowanie tupli
a, b = 1, 2
print(a)
print(b)
print(type((1, 2)))  # <class 'tuple'>

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # * - worek na pozostałe dane -> lista
print(a)
print(b)  # [2, 3]
print(type(b))  # <class 'list'>

print(tuple_names)  # ('Radek', 'Tomek', 'Zenek', 'Bartek')
imie1, *imie2, imie3 = tuple_names
print(imie2)  # ['Tomek', 'Zenek']
*imie1, imie2, imie3 = tuple_names
print(imie1)  # ['Radek', 'Tomek']

lista = list(tuple_names)
print(lista)
print(type(lista))
print(len(tuple_names))  # 4 - długość tupli

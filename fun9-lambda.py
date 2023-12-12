# funkcja lambda - skrócony zapis funkcji

odejmij = lambda a, b: a - b  # domyślnie ma return
print(odejmij(9, 8))

# def odejmij(a, b):
#     return a - b


oblicz_vat = lambda cena, vat=8: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 23))

lista = [1, 2, 3, 4, 5, 55, 66, 100]
for i in lista:
    print(i * 2)

print([i * 2 for i in lista])  # [2, 4, 6, 8, 10, 110, 132, 200]


def zmien(x):
    return x * 2


# map()
print(f"Zastosowanie map() {list(map(zmien, lista))}")
# Zastosowanie map() [2, 4, 6, 8, 10, 110, 132, 200]
print(f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map() [2, 4, 6, 8, 10, 110, 132, 200]
# filter()
print(f"Zastosowanie filter() {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter() [1, 2]
print(f"Zastosowanie filter() {list(filter(lambda x: x > 8, lista))}")
print(f"Zastosowanie filter() {list(filter(lambda x: 3 < x < 20, lista))}")
# Zastosowanie filter() [4, 5]

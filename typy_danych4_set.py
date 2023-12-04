# set - zbior - przechowuje unikalne wartości
# nie zachowuje kolejności podcczas dodawania elemntów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # set() - zamiana na set
print(lista)  # [44, 55, 66, 777, 33, 22, 11, 33, 11]
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

zb2 = set()  # tworzenie pustego seta
print(zb2)  # set()

# dodawanie elemntów do zbioru
zb2.add(2)
zb2.add(2)
zb2.add(3)
zb2.add(5)
zb2.add(3)
zb2.add(3)
print(zb2)  # {2, 3, 5}

print(zbior)
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# pop() - usunięcie pierwszego elementu z listy
print(zbior.pop())  # 33
print(zbior.pop())  # 66
print(zbior.pop())  # 777
print(zbior.pop())  # 11

# usunięcie elemntu ze zbioru
zbior.remove(44)
print(zbior)  # {18, 22, 55}

print(sorted(zbior))  # dostaniemy posortowana liste [18, 22, 55]

zbior2 = {667, 44, 18, 52, 55, 22, 687, 62, 999, 999}
print(zbior2)  # {999, 44, 687, 18, 52, 22, 55, 667, 62}
zbior.add(17)
print(zbior | zbior2)  # suma zbiorów {999, 44, 687, 17, 18, 52, 22, 55, 667, 62}
print(zbior.union(zbior2))  # {999, 44, 687, 17, 18, 52, 22, 55, 667, 62}
print(zbior)
print(zbior2)
# zbiory nie zostały modyfikowane
zbior3 = {8, 9, 10}
print(zbior.union(zbior2, zbior3))  # suma trzech zbiorow

# cześc wspolna
print(zbior & zbior2)  # {18, 22, 55}

# różnica zbiorów
print(zbior2 - zbior)  # {999, 44, 687, 52, 667, 62}
# {999, 44, 687, 18, 52, 22, 55, 667, 62} - {18, 22, 55} = {999, 44, 687, 52, 667, 62}

print(zbior2.difference(zbior))  # {999, 44, 687, 52, 667, 62}
print(zbior - zbior2)  # {17}

zbior4 = zbior.copy()
print(zbior4)  # {17, 18, 22, 55}
zbior.clear()  # usunięcie wszystkich elemntów ze zbioru zbior
print(zbior4)  # {17, 18, 22, 55}

zbior.update(zbior4)
print(zbior)  # {17, 18, 22, 55}
print(zbior4)

zb3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(sum(zb3))  # suma
print(min(zb3))  # wartosc minimalna
print(max(zb3))  # wartośc maxymalna
print(len(zb3))  # długośc
print(sorted(zb3))  # posortowana lista
# 45
# 1
# 9
# 9
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# lista - kolekcja, przechowuje dowolna ilosc danych dowolnego typu na raz
# zachowuje kolejnosc dodawania

lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

# append() - dodawanie do listy
lista.append("Radek")
lista.append("MAciek")
lista.append("Szymon")
lista.append("Jaśko")
lista.append("Zenek")
lista.append("Rafał")
print(lista)  # ['Radek', 'MAciek', 'Szymon', 'Jaśko', 'Zenek', 'Rafał']
#                    0        1         2       3(-3)      4(-2)       5(-1)
print(lista[0])
print(lista[-0])
print(lista[-1])
print(len(lista))  # długość listy
# print(lista[10])  # IndexError: list index out of range
print(lista[-3])
print(lista[0:3])  # ['Radek', 'MAciek', 'Szymon'] 0,1,2
print(lista[:3])  # ['Radek', 'MAciek', 'Szymon']
print(lista[-2:0])  # []
print(lista[0:-2])  # ['Radek', 'MAciek', 'Szymon', 'Jaśko']
print(lista[3:7])  # ['Jaśko', 'Zenek', 'Rafał']
print(lista[-5:0])
print(lista[0:-5])  # ['Radek']
print(lista[0:5:2])  # start stop krok
print(lista[0::2])  # ['Radek', 'Szymon', 'Zenek']

# ['Radek', 'MAciek', 'Szymon', 'Jaśko', 'Zenek', 'Rafał']
# ndpisanie elemntu na danym indeksie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'MAciek', 'Mikołaj', 'Jaśko', 'Zenek', 'Rafał']

# dodanie elementu pomiedzy elemnty we wskazanym miejscu
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'MAciek', 'Mikołaj', 'Jaśko', 'Zenek', 'Rafał']

# usuniecie elementu (pierwszy napotkane)
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Marcin', 'MAciek', 'Jaśko', 'Zenek', 'Rafał']

# sprawdzanie indeksu elemntu
indeks = lista.index("Marcin")
print(indeks)

# usuniecie leentu po numerze indeksu
print(lista.pop(indeks))  # Marcin - zwraca usuniety element
print(lista)
print(lista.pop())  # Rafał  ostatni element

a = 1
b = 3
a = b
print(a)
b = 7
print(a)

lista2 = lista  # kopia referencji - adresu w pamieci
lista3 = lista.copy()  # kopia elemntów listy do nowej listy
lista.clear()  # usuniecie wszystkich elemntów
print(lista2)  # []
print(lista)  # []
print(lista3)
print(id(lista2))  # 1361935710080
print(id(lista))  # 1361935710080
print(id(lista3))  # 1361935693760

liczby = [54, 999, 34, 22, 64.34, 687]
# liczby = [54, 999, 34, 22, 64, 687, "ABC"]  # TypeError: '<' not supported between instances of 'str' and 'int'
# liczby = [54, 999, 34, 22, 64.34, 687, "ABC"]  # TypeError: '<' not supported between instances of 'str' and 'float'

print(liczby)
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999], [22, 34, 54, 64.34, 687, 999]

lista_osoby = ['radek', 'ola', 'zenek']
lista_osoby.sort()
print(lista_osoby)  # ['ola', 'radek', 'zenek']
lista_osoby.sort(reverse=True)
print(lista_osoby)  # ['zenek', 'radek', 'ola']
lista_osoby.reverse()
print(lista_osoby)  # ['ola', 'radek', 'zenek']

liczby[3] = 6666
print(liczby)
# liczby[6] = 6666  # IndexError: list assignment index out of range

liczby.pop(3)
liczby.remove(54)

tekst = 'Python'
lista1 = [tekst]
print(lista1)  # ['Python']

# rozpakowanie sekwencji
lista2 = list(tekst)
print(lista2)  # ['P', 'y', 't', 'h', 'o', 'n']

tekst2 = "Radek Radek"
lista3 = list(tekst2)
print(lista3)  # ['R', 'a', 'd', 'e', 'k', ' ', 'R', 'a', 'd', 'e', 'k']
lista4 = list(lista3)
print(lista4)  # ['R', 'a', 'd', 'e', 'k', ' ', 'R', 'a', 'd', 'e', 'k']
krotka = tuple(lista4)
print(krotka)  # ('R', 'a', 'd', 'e', 'k', ' ', 'R', 'a', 'd', 'e', 'k')
print(type(krotka))  # <class 'tuple'>

# while - petla sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print("Komunikat!!")
    if licznik > 10:
        break  # przerwanie petli

print(licznik)
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat2!!!")

lista = []
lista2 = []
while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)  # ['4', '3', '2', '1', '4']
print(lista2)  # [1, 2, 3]

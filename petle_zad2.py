dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}
print(dictionary)
print(type(dictionary))

# wyswietli klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# wyswietlenie wartośc
for v in dictionary.values():
    print(v)

# para klucz wartosc
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski

import random

# random - generator liczb pseudolosowych
print(random)

print(random.randint(1, 6))  # int 1..6
print(random.randrange(1, 6))  # int 1..5
print(random.randrange(6))  # int 0..5
print(random.random())  # float 0.311104137644042 0..0.99999
print(random.random() * 10)  # float 7.739127131817154 0..9.99999

lista = [5, 7, 45, 34.56]
print(random.choice(lista))

lista_lotto = list(range(1, 46))  # wygeneruje od 1..45
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
print(random.choice(lista))

wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)

print(random.choices(lista_lotto, k=6))  # [21, 33, 11, 26, 21, 37] losowanie z powtórzeniami
print(random.sample(lista_lotto, 6))  # [1, 32, 24, 9, 45, 33]
print(random.sample(lista_lotto, k=6))  # [23, 5, 11, 18, 16, 33]

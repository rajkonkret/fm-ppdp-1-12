# instrukcja warunkowa
# uzależnia dzialnie programu od warunku
# instrukcje sterowania przepływem program
# if
# if warunek:
#   komenda_do wykonania gdy warunek spełniony
# po : musi byc conjmniej jedna komenda pythona

# odp = True
odp = False
if odp:
    print("Brawo")  # po : obowiązkowo wcięcie 4 spacje
else:
    print("Warunek False")
print("Dalsza cześc programu")

if odp:
    pass  # nic nie rób

print("Dalej")
#
# podatek = 0.9  # 90%
# zarobki = float(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:  # od 10000..29999
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Zapłacisz {zarobki * podatek:.2f} pln")
suma_zam = 150
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabacik {rabacik}")

rabat = 25 if suma_zam > 150 else 0
print(f"Rabacik {rabat}")

# zasymulujemy system anali logów
# dane przyjda w zmiennych
# na podstawie wartości tych zmiennych bedziemy mieli rózne działanie
# console, email -> inny
# error -> critical, medium, -> inny
# w przypadku błedu z konsoli wypiszemy komunikat
error_mesage = "Stało się coś strasznego"
error = "critical"
alert_system = 'console'
if alert_system == 'console':
    print(error_mesage)
elif alert_system == 'email':
    if error == 'critical':
        print("Masz błąd krytyczny")
    elif error == 'medium':
        print("Ostrzeżenie")
    else:
        print("Bład inny, idź na kawę")
else:
    print("Nie znam takiego systemu")
# napisac program test
odp = input("Podaj datę Chrztu Polski")
if odp == "966":
    print("Prawidłowa odpowiedź")
else:
    print("Błedna odpowiedź")

odp = input("Podaj imie")
if odp.upper() in ["RADEK", "TOMEK"]:
    print("Odpowiedź prawidłowa")
else:
    print("Bład")

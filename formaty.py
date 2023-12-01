user = "Tomek"  # str
wiek = 39  # int
wersja = 3.9000001  # <class 'float'>
print(type(wersja))
liczba = 123456789123  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %d masz teraz %s lat" % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit
print("Witaj %(user)s, masz teraz %(age)d " % {"user": user, "age": wiek})
# Witaj Tomek, masz teraz 39

print(f'Witaj {user}, masz teraz {wiek} lat.')  # f-string - string sformatowany
print("Uzywamy wersji pythona  %i " % 3)
print("Uzywamy wersji pythona  %f " % 3.8)  # float Uzywamy wersji pythona  3.800000
print("Uzywamy wersji pythona  %.1f " % 3.8)  # Uzywamy wersji pythona  3.8
print("Uzywamy wersji pythona  %.2f " % 3.8)  # Uzywamy wersji pythona  3.8
print("Uzywamy wersji pythona  %.0f " % 3.8)  # Uzywamy wersji pythona  4
print("Uzywamy wersji pythona  %.f " % 3.8)  # Uzywamy wersji pythona  4
# wykonuje zaokrąglenie
print(f"Używamy wersji python: {wersja}")
print(f"Używamy wersji python: {wersja:.1f}")
print(f"Używamy wersji python: {wersja:.2f}")  # Używamy wersji python: 3.90
print(f"Używamy wersji python: {wersja:.0f}")  # Używamy wersji python: 3.90
wersja = 134.89999
print(f"Używamy wersji python: {wersja:1.2f}")  # Używamy wersji python: 3.90
print(f"Używamy wersji python: {wersja:20f}")  # Używamy wersji python:           134.899990

print(f"{user:>20}")  # "               Tomek"
print(f"{user:<20}")  # "Tomek              "
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 123456789123
print("Nasza duza liczba {:,}".format(liczba))  # Nasza duza liczba 123,456,789,123
# zamienic , na spacje lub kropke
print("Nasza duza liczba {:,}".format(liczba).replace(",", " "))  # Nasza duza liczba 123 456 789 123
print("Nasza duza liczba {:,}".format(liczba).replace(",", "."))  # Nasza duza liczba 123 456 789 123
print(f"Liczba {liczba:,}".replace(",", " "))  # Liczba 123 456 789 123

try:
    # print(5 / 0)  # ZeroDivisionError: division by zero
    # print("a" / 2)
    # print(10 + "2")
    # print(int("A"))
    print(1 + 2)
except ZeroDivisionError:
    print("Nie dziel prze zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład", e)
else:
    print("Tylko gdy nie ma błedu")
finally:
    print("Wykona się niezależnie czy błąd wystąpi czy nie")

print("Dalsza cześć programy")
# try - except [else,finally]
# program kalkulator
# ma wyswietlic menu - dodawanie, odejmowanie, mnozenie, dzielenie
# ma uzyc petli while
# moze byc if lu match case
# ma ładnie wydrukować wynik działania
# Dodawanie 1 + 6 = 7
print(eval("2 + 5"))  # 7

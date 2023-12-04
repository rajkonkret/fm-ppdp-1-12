# match case od python 3.10

lista = []
# lang = input("Podaj znany Ci język programowania ")
lang = [1, 2, 3]
match lang:
    case "python":
        print("Lubię pythona")
        lista.append(lang)
    case "java":
        print("Java to kawa")
        lista.append(lang)
    case [a, b, c]:
        print(f"Lista z trzeba elementami {a} {b} {c}")
    case _:  # wartośc domyślna
        print("Nie znam takiego języka")

print(lista)

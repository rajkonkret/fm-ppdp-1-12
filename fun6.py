# funkcja, któa oblicza średnią

def liczby(name=None, *cyfry):
    print(cyfry)  # (1, 2, 3, 4, 5)
    suma = 0
    try:
        for cy in cyfry:
            suma += cy
        count = len(cyfry)
        print(f"Uczen {name} Srednia {suma / count}")
    except Exception as e:
        print("Bład", e)


liczby(1, 2, 3, 4, 5)
liczby()
liczby('Radek', 1, 2, 3, 4, 5, 6)
